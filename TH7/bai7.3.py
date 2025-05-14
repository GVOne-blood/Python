from abc import ABC, abstractmethod


class Account:
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


def check_amount(amount):
    if amount < 0:
        print("So tien phai > 0 ")
        return
    pass


class SavingAccount(Account):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        check_amount(amount)
        self.balance += amount
        print("Gui tien thanh cong ")

    def withdraw(self, amount):
        check_amount(amount)
        if self.balance < amount:
            print("Rut tien khong thanh cong do so du khong du ")
        else:
            print("Rut thanh cong ")

    def get_balance(self):
        print(f"So du hien tai {self.balance}")


class CheckingAccount(Account):
    def __init__(self, balance, limit):
        self.balance = balance
        self.limit = limit

    def deposit(self, amount):
        check_amount(amount)
        self.balance += amount
        print("Gui tien thanh cong ")

    def withdraw(self, amount):
        check_amount(amount)
        temp = self.balance
        temp += self.limit
        if temp < amount:
            print("Rut tien khong thanh cong do so du khong du ")
        else:
            print("Rut thanh cong ")
            self.balance -= amount

    def get_balance(self):
        print(f"So du hien tai {self.balance}")


sa = SavingAccount(10000)
sa.get_balance()
sa.withdraw(20000)
sa.get_balance()

ca = CheckingAccount(100000, 10000)
ca.get_balance()
ca.withdraw(110000)
ca.get_balance()
ca.withdraw(10000)