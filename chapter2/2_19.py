investment = eval(input("Enter investment amount: $"))
annualRate = eval(input("Enter annual interest rate: "))
years = eval(input("Enter number of years: "))

monthlyRate = annualRate / 1200
numMonths = years *  12

futureValue = round(investment * ( 1 + monthlyRate ) ** numMonths, 2)

print("Accumulated value is: $", futureValue)
