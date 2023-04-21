from datetime import datetime
from DBmanager import DatabaseManager
from CRUD import Model

db_config = {
    "dbname": "finance",
    "user": "postgres",
    "password": "@bb@s1366"
}

# Initialize the database manager
db_manager = DatabaseManager('finance', 'postgres', '@bb@s1366')


class User(Model):
    table_name = 'users'
    columns = {'id': 'int', 'name': 'varchar(20)'}

    def __init__(self):
        pass


User.create_table(db_manager)

User.insert_data(db_manager, id='3', name='\'ali\'')




# Define the base Model class
# class Model:
#     def __init__(self, db_manager, table_name, fields):
#         self.db_manager = db_manager
#         self.table_name = table_name
#         self.fields = fields
#
#     def create_table(self):
#         fields_str = ",".join([f"{field} {self.fields[field]}" for field in self.fields])
#         query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({fields_str})"
#         self.db_manager.execute_query(query)
#
#     def create_record(self, values):
#         fields_str = ",".join(self.fields)
#         placeholders = ",".join(["%s"] * len(values))
#         query = f"INSERT INTO {self.table_name} ({fields_str}) VALUES ({placeholders})"
#         self.db_manager.execute_insert(query, values)
#
#     def read(self, conditions=None):
#         query = f"SELECT * FROM {self.table_name}"
#         params = None
#         if conditions:
#             query += " WHERE " + conditions[0]
#             params = conditions[1]
#         return self.db_manager.execute_query(query, params)
#
#     def update(self, values, conditions=None):
#         set_clause = ",".join([f"{field}=%s" for field in self.fields])
#         query = f"UPDATE {self.table_name} SET {set_clause}"
#         params = values
#         if conditions:
#             query += " WHERE " + conditions[0]
#             params += conditions[1]
#         self.db_manager.execute_insert(query, params)
#
#     def delete(self, conditions=None):
#         query = f"DELETE FROM {self.table_name}"
#         params = None
#         if conditions:
#             query += " WHERE " + conditions[0]
#             params = conditions[1]
#         self.db_manager.execute_insert(query, params)
#
# # Define the User class
# class User(Model):
#     def __init__(self, db_manager):
#         table_name = "users"
#         fields = {
#             "id": "serial primary key",
#             "username": "text unique",
#             "password": "text",
#             "email": "text unique"
#         }
#         super().__init__(db_manager, table_name, fields)
#         self.create_table()
#
#     def create_user(self, username, password, email):
#         values = (username, password, email)
#         self.create_record(values)
#
#     def get_user_by_username(self, username):
#         conditions = ("username=%s", (username,))
#         results = self.read(conditions)
#         return results[0] if results else None
#
# # Define the Post class
# class Post(Model):
#     def __init__(self, db_manager):
#         table_name = "posts"
#         fields = {
#             "id": "serial primary key",
#             "title": "text",
#             "content": "text",
#             "created_at": "timestamp default now()",
#             "user_id": "integer references users(id) on delete cascade"
#         }
#         super().__init__(db_manager, table_name, fields)
#         self.create_table()
#
#     def create_post(self, title, content, user_id):
#         values = (title, content, user_id)
#         self.create_record(values)
#
#     def get_post_by_id(self, post_id):
#         conditions = ("id=%s", (post_id,))
#         results = self.read