userNum = eval(input("Please enter a 4 digit number: "))

num1 = userNum // 1000
num2 = (userNum // 100) % 10
num3 = (userNum // 10) % 10
num4 = userNum % 10

print(num1)
print(num2)
print(num3)
print(num4)
