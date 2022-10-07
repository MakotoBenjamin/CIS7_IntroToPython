# Receive the amount
amount = eval(input("Enter an amount, for example, 11.56: "))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = remainingAmount // 100
remainingAmount = remainingAmount % 100

# Find the number of quarters in the remaining amount
numberOfQuarters = remainingAmount // 25
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = remainingAmount // 10
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = remainingAmount // 5
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display the results
print("Your amount", amount, "consists of")
if numberOfOneDollars > 0:
    print("\t", numberOfOneDollars, "dollars") if numberOfOneDollars>1 else print("\t", numberOfOneDollars, "dollar")
if numberOfQuarters > 0:
    print("\t", numberOfQuarters, "quarters") if numberOfQuarters>1 else print("\t", numberOfQuarters, "quarter")
if numberOfDimes > 0:
    print("\t", numberOfDimes, "dimes") if numberOfDimes>1 else print("\t", numberOfDimes, "dime")
if numberOfNickels > 0:
    print("\t", numberOfNickels, "nickels") if numberOfNickels>1 else print("\t", numberOfNickels, "nickel")
if numberOfPennies > 0:
    print("\t", numberOfpennies, "pennies") if numberOfPennies>1 else print("\t", numberOfPennies, "penny")
