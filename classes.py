# By Shubham Jha (Code with SJ)
# Subscribe to My Youtube Channel: https://www.youtube.com/@CodewithSJ
# Video Explanation: 


class Human:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_data(self):
        print(f"Name is {self.name} and the age is {self.age}")


obj1 = Human("Shubham", 27)
obj1.print_data()


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance!")
            self.check_balance()
    
    def check_balance(self):
        print(
            f"Your account {self.account_number} "
            f"balance is {self.balance}"
        )

account1 = BankAccount("12345", 1000)
account1.check_balance()
account1.withdraw(500)
account1.check_balance()
account1.withdraw(1000)
# account1.check_balance()
account1.deposit(500)
account1.check_balance()


account2 = BankAccount("54321")
account2.deposit(1846)
account2.check_balance()








