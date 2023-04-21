from BaseModel import BaseModel


class Person(BaseModel):
    def __init__(self, type=None, date=None, amount=None, category=None, description=None):
        self.type = type
        self.date = date
        self.amount = amount
        self.category = category
        self. description = description

    def create(self):
        query = "INSERT INTO finance(type, date, amount, category, description)" \
                " VALUES (%s,%s,%s,%s,%s), ('income', '2023-04-21', 1000000, 'sale', 'phone');"
        params = (self.type, self.date, self.amount, self.category, self.description)
        result = self.execute_query(query, params)

    def read(self, conditions=None):
        pass