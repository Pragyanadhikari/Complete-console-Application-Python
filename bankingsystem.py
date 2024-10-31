# 2. Banking System
# • Description: Develop a console banking application that simulates bank account management. Implement classes for Account, SavingsAccount, and CurrentAccount. Include functionalities for deposits, withdrawals, and balance inquiries.
# • OOP Concepts: Inheritance (different account types), Encapsulation (keeping account data private), and Abstract Classes (defining common methods).
from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,name,balance=0):
        self.name=name
        self.__balance=balance
    @abstractmethod
    def account_type(self):
        pass
    def deposit(self,amt):
        if amt>0:
            self.__balance+=amt
            print(f"{self.name} deposited {amt} and new balance is {self.__balance}.")
        else:
            print("You cannot deposit amount less than 0.")
    def withdraw(self,amt):
        if self.__balance<amt:
            print("You do not have sufficient balance to withdraw.")
        else:
            self.__balance-=amt
            print(f"{self.name} withdrew {amt} and new balance is: {self.__balance}.")

    def inquiry_balance(self):
        print(f"Your current balance is: {self.__balance}.")
    
    def getBalance(self):
        return self.__balance
    
    @abstractmethod
    def get_account_number():
        pass
    
    
    def show_account_details(self):
        print(f"Name: {self.name}\t\t Account Number={self.get_account_number()}\t\t Account type :{self.account_type()} \t\tBalance:{self.__balance}")
        print()

class SavingAccount(Account):
    saving_account_id='SA-987654'
    user_number=1
    def __init__(self, name, balance=0):
        super().__init__(name, balance)
        self.saving_account_number=SavingAccount.saving_account_id+str(SavingAccount.user_number)
        SavingAccount.user_number+=1
    def account_type(self):
        return "Saving Account"
    
    def apply_interest(self):
        interest=self.getBalance()*0.03
        self.deposit(interest)
        print(f"Interest amount {interest} is added to {self.name} account.")
    def get_account_number(self):
        length_of_id=len(self.saving_account_number)
        return self.saving_account_number[0:5]+'#'*(length_of_id-5)
    
class CurrentAccount(Account):
    current_account_id='CA-12345'
    user_number=1
    def __init__(self, name, balance=0):
        super().__init__(name, balance)
        self.current_account_number=CurrentAccount.current_account_id+str(CurrentAccount.user_number)
        CurrentAccount.user_number+=1
    def account_type(self):
        return "Current Account"
    def get_account_number(self):
        length_of_id=len(self.current_account_number)
        return self.current_account_number[0:5]+'#'*(length_of_id-5)

s1=SavingAccount("Pragyan",10000)
s2=SavingAccount("Hira")

c1=CurrentAccount("Rita",1000)
c2=CurrentAccount("Nita",200)

s1.deposit(1000)
s1.show_account_details()
s1.withdraw(800)

s2.show_account_details()

c1.deposit(10000)
c1.show_account_details()
c1.withdraw(5000)
c1.show_account_details()
c2.show_account_details()