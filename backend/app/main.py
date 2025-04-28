
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import auth, users
from .routers import manage_data, access_db
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(manage_data.router)
app.include_router(access_db.router)