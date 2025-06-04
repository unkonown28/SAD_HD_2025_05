class MySQLDatabase:
    def connect(self):
        print("Connecting to MySQL")

class App:
    def __init__(self):
        self.db = MySQLDatabase()
        self.db.connect()
