def computeCommission(salesAmount):
    """    
    commission = 0.00
    
    if salesAmount >= .01 and salesAmount <= 5000:
        commission = salesAmount * .08

    elif salesAmount >= 5000.01 and salesAmount <=10000:
        commission = salesAmount * .1

    elif salesAmount >= 10000.01:
        commission = salesAmount * .12

    else:
        print("Invalid Entry")

    """

    if salesAmount >= 10000.01:
        commission = 5000 * 0.08 + 5000 * 0.1 + (salesAmount - 10000) * 0.12
    elif salesAmount >= 5000.01:
        commission = 5000 * 0.08 + (salesAmount - 5000) * 0.10
    else:
        commission = salesAmount * 0.08

    return commission

    
def main():

    print(format("Sales Amount", '<15'),format("Commission",'>15'))

    for i in range(10000,100001,5000):
        print(format(i,'<14d'), format(computeCommission(i),'>15.1f'))
main()
