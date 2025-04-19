from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "shatel-super-secret"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as E:
        print(f"JWT Decode Error: {E}")
        raise HTTPException(status_code=401, detail="Invalid token")


def has_permission(permission: str):
    def checker(user = Depends(get_current_user)):
        print(user.get("permissions", []))
        print(permission)
        if permission not in user.get("permissions", []):
            raise HTTPException(status_code=403, detail="Permission denied")
    return checker
