class Account:

    def __init__(self,userID = 0, balance = 100.00, annualInterestRate = 0.00):
        self.__userID = userID
        self.__balance = balance
        self.__annualInterestRate = annualInterestRate

    def setId(self, userID):
        self.__userID = userID

    def setBalance(self, balance):
        self.__balance = balance

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getId(self):
        return self.__userID

    def getBalance(self):
        return self.__balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def getMonthlyInterestRate(self):
        monthlyInterestRate = self.__annualInterestRate / 1200

        return monthlyInterestRate

    def getMonthlyInterest(self):
        monthlyInterest = self.__balance * self.getMonthlyInterestRate()

        return monthlyInterest

    def withdraw(self, withdrawalAmount = 0.0):
        if withdrawalAmount > self.__balance:
            print("Withdrawal amount greater than current balance. Unable to process request.")
        
        elif withdrawalAmount < 0:
            print("Cannot withdraw negative value. Unable to process request.")

        else:
            self.__balance -= withdrawalAmount

            print("You withdrew ${:.2f}".format(withdrawalAmount) + ".\nYou now have ${:.2f}".format(self.__balance) + " remaining in your account.")

    def deposit(self, depositAmount = 0.0):
        if depositAmount < 0:
            print("Cannot deposit negative value. Unable to process request.")
        
        else:
            self.__balance += depositAmount

            print("You deposited $" + str(depositAmount) + ".\nYou now have $" + str(self.__balance) + " in your account.")
