class car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def show(self):
        print(f"{self.make}, {self.model}")
    
mycar = car("TOYOTA", "RAV4")
mycar.show()

# Inheritance - Lexus class inherits car class
class Lexus(car):
    def __init__(self, make, model, color, year):
        super().__init__(make, model)
        self.color = color
        self.year = year
    
    def show(self):
        print(f"{self.make}, {self.model}, {self.color}, {self.year}")

mylexus = Lexus("LX", "RX350", "Red", 2024)
mylexus.show() # Polymorphism child show() method is called instead of parent


# Encapsulation -- To access private attributes and methods
class BankAccount:
    def __init__(self, account_number):
        self.__account_number = account_number  # private attribute
    
    def getAccountNumber(self):
        return self.__account_number

myAccount = BankAccount("123456789")
myAccount.getAccountNumber()