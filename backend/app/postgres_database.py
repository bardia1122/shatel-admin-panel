import psycopg2
import json
from passlib.hash import bcrypt

DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/postgres"


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

