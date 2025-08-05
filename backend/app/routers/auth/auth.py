# from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from typing import List

# from ... import schemas
# from ...database import models
# from ...database.dependencies import get_db
# from ...utils.auth import hash_password, verify_password, create_access_token

# router = APIRouter()

# @router.post("/register", response_model=schemas.UserOut)
# def register(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.username == user_data.username).first()
#     if user:
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Username already registered"
#         )
    
#     hashed_password = hash_password(user_data.password)

#     new_user = models.User(
#         username=user_data.username,
#         password=hashed_password,
#         role=user_data.role,
#         permissions=user_data.permissions
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
    
#     return new_user

# @router.post("/login", response_model=schemas.Token)
# def login(user_data: schemas.UserLogin, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.username == user_data.username).first()
    
#     if not user or not verify_password(user_data.password, user.password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
    
#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}