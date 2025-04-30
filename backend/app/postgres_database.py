import psycopg2
import json
from passlib.hash import bcrypt
from .classes import KB
DB_CONFIG = {
    "dbname": "postgres",
    "user": "myuser",
    "password": "mypassword",
    "host": "localhost",
    "port": "5432"
}

def add_user(username, password, role, permissions):
    conn = psycopg2.connect(
        dbname="postgres",
        user="myuser",
        password="mypassword",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    try:
        hashed_password = bcrypt.hash(password)  # auto-hash here
        insert_query = """
        INSERT INTO users (username, password, role, permissions)
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(insert_query, (
            username,
            hashed_password,
            role,
            json.dumps(list(permissions))
        ))
        conn.commit()
        print("User inserted.")
    except Exception as e:
        conn.rollback()
        print("error:", e)
    finally:
        cur.close()
        conn.close()


def get_user_from_db(username: str):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        cur.execute("SELECT username, password, role, permissions FROM users WHERE username = %s", (username,))
        row = cur.fetchone()
        if row:
            return {
                "username": row[0],
                "hashed_password": row[1],
                "roles": [row[2]],
                "permissions": json.loads(row[3])
            }
    finally:
        cur.close()
        conn.close()
    return None

def add_kb_to_db(kb: KB):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        name = kb.get_name()
        role = kb.get_permission()
        insert_query = """
        INSERT INTO kbs (name, role)
        VALUES (%s, %s)
        """
        cur.execute(insert_query, (name, role))
        conn.commit()
    finally:
        cur.close()
        conn.close()
    return None

def get_all_kb(user_role):
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()
    try:
        if user_role == "admin":
            cur.execute("SELECT name FROM kbs WHERE role IN ('admin', 'user')")
        elif user_role == "user":
            cur.execute("SELECT name FROM kbs WHERE role = 'user'")
        else:
            return []
        return [{"name": row[0]} for row in cur.fetchall()]
    finally:
        cur.close()
        conn.close()
