def test():
    
    count = 1
    
    print("---- Test ----")

    for i in range(49,91):
        
        if count % 10 == 0:
            print(chr(i))
        else:
            print(chr(i), end = " ")
        
        count += 1

def printChars(ch1, ch2, numberPerLine):
    
    count = 1

    for i in range(ch1, ch2+1):
    
        if count % numberPerLine == 0:
            print(chr(i))
        else:
            print(chr(i), end = " ")

        count += 1

def main():
    
    print("\nPlease enter two decimal numbers between 0 & 127. The program will output all of the corresponding ASCII characters between the two numbers.")
        
    userNum1, userNum2 = eval(input("Enter your numbers separated by a comma: "))
    
    while userNum1 < 0 or userNum2 < 0 or userNum1 > 127 or userNum2 > 127:
        print("\n----Invalid Entry---\n")
        userNum1, userNum2 = eval(input("Retry with valid entries. Enter your numbers separated by a comma: "))


    charsToPrint = eval(input("Enter the number of characters you want each line to print: "))

    if userNum2 < userNum1:
        userNum1, userNum2 = userNum2, userNum1

    printChars(userNum1, userNum2, charsToPrint)

#test()
main()

