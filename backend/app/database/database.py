from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://appuser:appsecret@app-db:5434/appdb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


# import psycopg2
# import json
# from passlib.hash import bcrypt
# from ..classes import KB


# # Use the service name "db" as the host, as defined in docker-compose.yml
# DB_CONFIG = {
#     "dbname": "postgres",
#     "user": "postgres",
#     "password": "postgres",
#     "host": "db",
#     "port": "5432"
# }

# def add_user(username, password, role, permissions):
#     conn = psycopg2.connect(**DB_CONFIG)
#     cur = conn.cursor()

#     try:
#         hashed_password = bcrypt.hash(password)
#         insert_query = """
#         INSERT INTO users (username, password, role, permissions)
#         VALUES (%s, %s, %s, %s)
#         """
#         cur.execute(insert_query, (
#             username,
#             hashed_password,
#             role,
#             json.dumps(list(permissions))
#         ))
#         conn.commit()
#         print("User inserted.")
#     except Exception as e:
#         conn.rollback()
#         print("error:", e)
#     finally:
#         cur.close()
#         conn.close()


# def get_user_from_db(username: str):
#     conn = psycopg2.connect(**DB_CONFIG)
#     cur = conn.cursor()
#     try:
#         cur.execute("SELECT username, password, role, permissions FROM users WHERE username = %s", (username,))
#         row = cur.fetchone()
#         if row:
#             return {
#                 "username": row[0],
#                 "hashed_password": row[1],
#                 "roles": [row[2]],
#                 "permissions": json.loads(row[3])
#             }
#     finally:
#         cur.close()
#         conn.close()
#     return None

# def add_kb_to_db(kb: KB):
#     conn = psycopg2.connect(**DB_CONFIG)
#     cur = conn.cursor()
#     try:
#         name = kb.get_name()
#         role = kb.get_permission()
#         insert_query = """
#         INSERT INTO kbs (name, role)
#         VALUES (%s, %s)
#         """
#         cur.execute(insert_query, (name, role))
#         conn.commit()
#     finally:
#         cur.close()
#         conn.close()
#     return None

# def get_all_kb(user_role):
#     conn = psycopg2.connect(**DB_CONFIG)
#     cur = conn.cursor()
#     try:
#         if user_role == "admin":
#             cur.execute("SELECT name FROM kbs WHERE role IN ('admin', 'user')")
#         elif user_role == "user":
#             cur.execute("SELECT name FROM kbs WHERE role = 'user'")
#         else:
#             return []
#         return [{"name": row[0]} for row in cur.fetchall()]
#     finally:
#         cur.close()
#         conn.close()