
from fastapi import APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from passlib.hash import bcrypt

router = APIRouter()

# Dummy user
fake_user = {
    "username": "admin",
    "password_hash": bcrypt.hash("password123")
}

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    if username != fake_user["username"] or not bcrypt.verify(password, fake_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    return JSONResponse(content={"message": "Login successful", "username": username})
