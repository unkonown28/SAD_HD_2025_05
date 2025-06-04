class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        print(f"Calculating salary for {self.name}")

    def save_to_database(self):
        print(f"Saving {self.name} to the database")
