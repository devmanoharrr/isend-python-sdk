import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

def is_valid_api_key(api_key):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM accounts WHERE api_key = %s", (api_key,))
            result = cursor.fetchone()
        conn.close()
        return bool(result)
    except Exception as e:
        print("DB error:", e)
        return False
