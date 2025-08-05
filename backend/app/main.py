
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import users
from .routers.access import access_db, access_kb
from backend.app.routers.auth import login, register
from backend.app.routers.access import access_db, access_kb
from .routers import manage_data
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router, prefix="/auth", tags=["Auth"])
app.include_router(register.router, prefix="/auth", tags=["Auth"])
app.include_router(access_kb.router, prefix="/access", tags=["Access"])
app.include_router(access_db.router, prefix="/access", tags=["Access"])
app.include_router(users.router)
# app.include_router(manage_data.router)
# app.include_router(access_db.router)
# app.include_router(access_kb.router)