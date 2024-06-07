import os
import psycopg2 as psql
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv('db_database'),
            user=os.getenv('db_user'),
            password=os.getenv('db_password'),
            host=os.getenv('db_host'),
            port=os.getenv('db_port')
        )
        cursor = db.cursor()
        cursor.execute(query)
        database = ['create', 'delete', 'update', 'insert']
        if query_type in database:
            db.commit()
            if query_type == 'create':
                return f"created successfully"
            return f"{query_type} query successful"
        else:
            return cursor.fetchall()


class Check:
    @staticmethod
    def phone(phone_number: str):
        query = f"SELECT * FROM admin WHERE phone_number='{phone_number}'"
        data = Database.connect(query, query_type='select')
        if len(data) == 1:
            return True
        else:
            return False

    @staticmethod
    def admin_password(password: str):
        query = f"SELECT * FROM admin WHERE password = '{password}'"
        data = Database.connect(query, query_type='select')
        if len(data) == 1:
            return True
        else:
            return False


class Person:
    @staticmethod
    def phone(phone_number: str):
        query = f"SELECT * FROM persons WHERE phone_number='{phone_number}'"
        data = Database.connect(query, query_type='select')
        if len(data) == 1:
            return True
        else:
            return False

    @staticmethod
    def password(password: str):
        query = f"SELECT * FROM persons WHERE password = '{password}'"
        data = Database.connect(query, query_type='select')
        if len(data) == 1:
            return True
        else:
            return False
