''' this is an object oriented programming example,
it demonstrates the concepts of inheritance , encapsulation and polymophisim
'''
#parent class 
class BankAccount:
    #constructor method
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder #public
        self.__balance = balance #private

    #deposit ()method
    def deposit(self,amount):
        """" ALLOWS DEPOSIT OF MONEY INTO THE ACCOUNT TO AFF TO THE HIDDEN""" 
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposited amount must be positive")   

    #withdraw () method
    def withdraw(self, amount):
        """allows withdrawal of money into the account to reduce the hidden balance"""
        if(0 <amount<= self.__balance):
            self.__balance -= amount
            print(f"Withdrew {amount}. Remaining balance{self.__balance}") 
        else:
            print("Insufficient funds")

    #get_balance()method
    def get_balance(self):
        "ALLOWS VIEWING OF BALANCE"
        return self.__balance
#end of parent class
#  creating a child class that will inherit from parent bankaccount
# 
# child class saving classaccount
class SavingAccount(BankAccount):
    def __init__(self,account_holder,balance,interest_rate):  
        """chilconstructor which uses the parent att but also adds an attribute interest_rate"""
        super().__init__(account_holder, balance)   #caliing the parent constructor to define and set
        self.interest_rate = interest_rate #public

    def apply_interest(self):
        "savingaccount have a unique methos that applies interest to the balance"
        interest = self.get_balance() * self.interest_rate/100
        self.deposit(interest)
        print(f"Interest of {interest} applied. New Balance:{self.get_balance()}")

class checkingAccount(BankAccount):
    def __init__(self,account_holder, balance, overdraft_limit):
        """child con which uses the parent but also adds an extra feature of overdraft-limit"""
        super().__init__(account_holder,balance)
        self.overdraft_limit = overdraft_limit

    def withdraw (self, amount): 
        """polymophisim applies by having a child class withdrew() method overide the parent withdew() method to allow for overdraft"""

        if amount <= (self.get_balance() + self.overdraft_limit):
            self.deposit (-amount) #we will deposit a -ve amount indicating an overdraft
            print(f"Overdraft allowed. Withdrawn: {amount}. Remaining balance{self.get_balance()}")
        else:
            print("Withdrawal exceeds overdraft limit")  

#ctual program
savings = SavingAccount('Wanja', 1000, 5) #accountholder
checking = checkingAccount('Wanja', 500, 200)

savings.deposit(500)
savings.apply_interest()

checking.withdraw(900)
checking.withdraw(600)
