from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from passlib.hash import bcrypt
from jose import jwt
from datetime import datetime, timedelta

router = APIRouter()
SECRET_KEY = "shatel-super-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

fake_users_db = {
    "admin": {
        "username": "admin",
        "hashed_password": bcrypt.hash("admin123"),
        "roles": ["admin"],
        "permissions": ["view_logs", "access_db", "manage_data"]
    },
    "viewer": {
        "username": "viewer",
        "hashed_password": bcrypt.hash("viewer123"),
        "roles": ["viewer"],
        "permissions": ["view_logs"]
    }
}

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    user = fake_users_db.get(username)
    if not user or not bcrypt.verify(password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token({
        "sub": username,
        "roles": user["roles"],
        "permissions": user["permissions"]
    })
    return JSONResponse(content={"access_token": token, "token_type": "bearer"})
