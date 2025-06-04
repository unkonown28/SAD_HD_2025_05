class Database:
    def connect(self):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connecting to MySQL")

class App:
    def __init__(self, database: Database):
        self.db = database
        self.db.connect()

# Usage
db = MySQLDatabase()
app = App(db)
