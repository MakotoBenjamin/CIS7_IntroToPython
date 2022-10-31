from AccountTemplate import Account

def main():
    account1 = Account(1122, 20000, 4.5)
    
    account1.withdraw(2500)
    account1.deposit(3000)
    
    print("\n-----------------------\n")

    print(
            "ID: {:d}".format(account1.getId()) + 
            "\nBalance: {:.2f}".format(account1.getBalance()) + 
            "\nMonthly Interest Rate: {:f}".format(account1.getMonthlyInterestRate()) + 
            "\nMonthly Interest: {:.2f}".format(account1.getMonthlyInterest())
            )

main()
