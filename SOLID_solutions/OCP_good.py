class Customer:
    def get_discount(self):
        return 0

class RegularCustomer(Customer):
    def get_discount(self):
        return 10

class VIPCustomer(Customer):
    def get_discount(self):
        return 20
