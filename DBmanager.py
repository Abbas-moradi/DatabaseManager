import psycopg2
from psycopg2 import pool


class DatabaseManager:
    def __init__(self, dbname, user, password, host='localhost', port=5432, pool_size=10):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.pool_size = pool_size
        self.pool = None

    def get_connection(self):
        try:
            self.pool = pool.SimpleConnectionPool(
                minconn=1, maxconn=self.pool_size,
                dbname=self.dbname, user=self.user,
                password=self.password, host=self.host,
                port=self.port
            )
            return self.pool.getconn()
        except psycopg2.Error as e:
            print("Error connecting to database:", e)
            raise

    def close_connection(self, conn):
        try:
            self.pool.putconn(conn)
        except psycopg2.Error as e:
            print("Error closing database connection:", e)
            raise

    def execute_query(self, query, params=None, fetch=False):
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(query, params)
            if fetch:
                result = cursor.fetchall()
                return result
            else:
                result = None
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("Error executing query:", e)
            raise
        finally:
            cursor.close()
            self.close_connection(conn)
        return result

    def begin_transaction(self):
        conn = self.get_connection()
        conn.autocommit = False
        return conn

    def commit_transaction(self, conn):
        try:
            conn.commit()
        except psycopg2.Error as e:
            conn.rollback()
            print("Error committing transaction:", e)
            raise
        finally:
            self.close_connection(conn)

    def rollback_transaction(self, conn):
        try:
            conn.rollback()
        except psycopg2.Error as e:
            print("Error rolling back transaction:", e)
            raise
        finally:
            self.close_connection(conn)


customer = DatabaseManager('finance', 'postgres', 'password')
                     
