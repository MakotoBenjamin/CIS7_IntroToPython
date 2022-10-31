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
    
    print("\nPlease enter two characters. The program will output all of the corresponding ASCII characters between the two entered values.")
        
    ch1, ch2 = input("Enter your characters separated by a comma: ").split()
   
  #  while userNum1 < 0 or userNum2 < 0 or userNum1 > 127 or userNum2 > 127:
  #      print("\n----Invalid Entry---\n")
  #      userNum1, userNum2 = eval(input("Retry with valid entries. Enter your numbers separated by a comma: "))

    charsToPrint = eval(input("Enter the number of characters you want each line to print: "))
    
    userNum1 = ord(ch1)
    userNum2 = ord(ch2)

    if userNum2 < userNum1:
        userNum1, userNum2 = userNum2, userNum1

    printChars(userNum1, userNum2, charsToPrint)

#test()
main()

