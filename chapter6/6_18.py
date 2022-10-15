import random

def printMatrix(n):
    for i in range(0,n):
        count = 1
        for x in range(0,n):
            if count % n == 0:
                print(random.randint(0,1))
            else:
                print(random.randint(0,1), end = " ")
        print()

def main():
    userNum = eval(input("Please enter a positive number: "))

    while userNum < 1:
        print("\n---Invalid Entry---\n")
        userNum = eval(input("Try again with valid value. Please enter a positive number: "))

    printMatrix(userNum)

main()
        
        
