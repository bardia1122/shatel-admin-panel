# from fastapi import APIRouter, Form, HTTPException
# from fastapi.responses import JSONResponse
# from passlib.hash import bcrypt
# from jose import jwt
# from datetime import datetime, timedelta
# import psycopg2
# import json
# from app.database.database import add_user
# from .database.database import get_user_from_db
# router = APIRouter()

# SECRET_KEY = "shatel-super-secret"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 180

# def create_access_token(data: dict):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# @router.post("/login")
# def login(username: str = Form(...), password: str = Form(...)):
#     user = get_user_from_db(username)
#     if not user or not bcrypt.verify(password, user["hashed_password"]):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
    
#     token = create_access_token({
#         "sub": username,
#         "roles": user["roles"],
#         "permissions": user["permissions"]
#     })
#     print(user["permissions"])
#     return JSONResponse(content={"access_token": token, "token_type": "bearer"})

# @router.post("/register")
# def register(
#     username: str = Form(...),
#     password: str = Form(...),
#     role: str = Form(...),
#     permissions: str = Form(...)  # comma-separated
# ):
#     # Check if user exists first
#     conn = psycopg2.connect(
#         dbname="postgres",
#         user="myuser",
#         password="mypassword",
#         host="localhost",
#         port="5432"
#     )
#     cur = conn.cursor()
#     try:
#         cur.execute("SELECT 1 FROM users WHERE username = %s", (username,))
#         if cur.fetchone():
#             raise HTTPException(status_code=400, detail="Username already exists")
#     finally:
#         cur.close()
#         conn.close()

#     try:
#         perm_list = [perm.strip() for perm in permissions.split(",")]
#         add_user(username, password, role, perm_list)
#         return {"msg": "User registered successfully."}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Registration failed: {e}")