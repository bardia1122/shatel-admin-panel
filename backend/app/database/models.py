from sqlalchemy import Column, Integer, String, JSON
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    permissions = Column(JSON)

class KB(Base):
    __tablename__ = "kbs"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String, index=True)
    
    role = Column(String)