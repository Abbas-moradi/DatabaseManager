from abc import ABC

from BaseCRUD import BaseCrud
from DBmanager import DatabaseManager

class Model:
    table_name = None
    columns = {}

    @classmethod
    def create_table(cls, dbmanager):
        query = f'CREATE TABLE IF NOT EXISTS {cls.table_name} ('
        query += ','.join([f'{col} {cls.columns[col]}' for col in cls.columns])
        query += f');'
        dbmanager.execute_query(query)

    @classmethod
    def read(cls, where=None):
        query = f'SELECT * FROM {cls.table_name} WHERE {where}'
        return DatabaseManager.execute_query(query, fetch=True)

    @classmethod
    def insert_data(cls, dbmanager, **kwargs):
        query = f'INSERT INTO {cls.table_name} ('
        query += ','.join(kwargs.keys())
        query += ')'
        query += 'VALUES ('
        query += ','.join(kwargs.values())
        query += f');'
        dbmanager.execute_query(query)

    def update(self, where=None):
        pass

    def delete(self, where=None):
        pass


