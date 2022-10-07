name = input("Enter employee's name: ")

#User enters info about their pay
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: $"))

#User enters withholding rates
federalRate = eval(input("Enter federal tax withholding rate: "))
stateRate = eval(input("Enter state tax withholding rate: "))

#Calculations
gross = hours * rate

federalWithholding = gross * federalRate
stateWithholding = gross * stateRate
totalDeductions = federalWithholding + stateWithholding

net = gross - totalDeductions

print("------------\nInfo:\n------------") 
print("\tEmployee Name: " + name)
print("\tHours Worked: " + format(hours, '.2f'))
print("\tPay Rate: $" + format(rate, '.2f'))
print("------------\nDeductions:\n------------\n\t" + 
        "Federal Withholding (" + format(federalRate, '.2%') + "): $" + format(federalWithholding, '.2f') + "\n\t" +
        "State Withholding (" + format(stateRate, '.2%') + "): $" + format(stateWithholding, '.2f') + "\n\t" +
        "Total Deduction: $" + format(totalDeductions, '.2f'))
print("------------\nPay Totals:\n------------") 
print("\tGross Pay: $" + format(gross, '.2f'))
print("\tNet Pay: $" + format(net, '.2f'))
        

