# 11. Budget Tracker
# • Description: Create a console application to manage personal finances. Implement classes for Expense, Income, and Budget. Include methods for adding and categorizing expenses and income, as well as generating reports.
# • OOP Concepts: Composition (budgets consist of expenses and income), Inheritance (different expense types), and Encapsulation (managing financial data).

class Expense:
    def __init__(self,on,amount,description):
        self.expense_on=on
        self.expense_amount=amount
        self.description=description
    
    def __str__(self):
        return f'Expense on: {self.expense_on}\nAmount: {self.expense_amount}\nDescription: {self.description}\n'
    
class Income:
    def __init__(self,source,amount):
        self.source=source
        self.amount=amount
    
    def __str__(self):
        return f'Source: {self.source}\nAmount: {self.amount}\n'
class Budget:
    def __init__(self):
        self.income_list=[]
        self.expense_list=[]
    
    def add_income(self,income):
        self.income_list.append(income)
    
    def add_expense(self,expense):
        self.expense_list.append(expense)
    
    def total_income(self):
        return sum(income.amount for income in self.income_list)
    
    def total_expense(self):
        return sum(expense.expense_amount for expense in self.expense_list)
    
    def report(self):
        print("*"*25)
        print("Income: ")
        for income in self.income_list:
            print(income)
        print(f"Total income: {self.total_income()}")
        print()
        print("Expense: ")
        for expense in self.expense_list:
            print(expense)
        print(f"Total expense: {self.total_expense()}")

        print(f"Saving: {self.total_income()-self.total_expense()}")

i1=Income("Business",100000)
i2=Income("Job",68000)
i3=Income("Rent",15000)

e1=Expense("Daily expense",50000,"Expense on daily item like food and cloth in a month.")
e2=Expense("Enjoyment",50000,"Spent on entertainment field every month")

b=Budget()
b.add_income(i1)
b.add_income(i3)
b.add_income(i2)
b.add_expense(e1)
b.add_expense(e2)

b.report()