---- # Midterm Review Notes ----

# Printing with print function, print without newline, print with formatted data
first= "John"
last = "Smith"
wage = 17.75

print("Employee:",first,last)
print("Wage: $", wage, "per hour")

#printing without new line
print("Employee:",first,last, end = "\t")
print("Wage:$",wage,"/per hour")
print("Wage:$"+str(wage)+"/per hour")

-------------------------------------------------------------------------------------------------------------------------------------------

#examples of format function
#s = string
#f = float
#d = int
#% = percentage

print(format(first, "10s")) 

#for floats & %, speficy decimal values by using .x where x is the number of decimal places you would like to display
print(format(wage, ".2f"))
print(format(1234, "5d"))

#outputs: 4.79% --> % format the number entered is multiplied by 100
print(format(0.04786, ".2%"))

-------------------------------------------------------------------------------------------------------------------------------------------

#Take user input
name = input("Enter name: ")  #string type
hours = eval(input("Enter hours: "))
x,y = eval(input("Enter center point coordinates seperated by comma: "))

-------------------------------------------------------------------------------------------------------------------------------------------

#Arithmetic operators, comparison operators, logic operators.
#Arithmetic operators: +, -, *, /, **, //, %

# // = integer divide

#Comparison operators: >, >=,<,<=,==,!=
#Logic operators: and, or, not
year = 2018
isLeapYear = (year%4==0 and year%100!=0) or (year%400==0)
if isLeapYear:
    days = 29
else:
    days = 28

-------------------------------------------------------------------------------------------------------------------------------------------

#Math functions, random number generation, string functions
import math
x = math.sqrt(49)

-------------------------------------------------------------------------------------------------------------------------------------------

import random
r1 = random.random() #float number between 0 and 1 ( not including 1)
r2 = random.randint(10,99) #random 2-digit integer 
r3 = random.randrange(10,100) #random integer 2-digit integer( 10 to 99)

-------------------------------------------------------------------------------------------------------------------------------------------

code = 100
char = "A"

#converts variable "x" into string data type
String = str(x)
ch = chr(code)  #converts from ascii code to character
acode = ord(char) #converts from character to ascii code

-------------------------------------------------------------------------------------------------------------------------------------------

#Conditional statement: if, if-else, if –elif-else
#Sample: Listing 4.6
#Sample: Exercise 4.11, 4.8
#for i in range(3):
#Ex 4.8
n1,n2,n3 = eval(input("Enter 3 numbers separated by commas: "))
if n1>n2:
    n1,n2=n2,n1
if n2>n3:
    n2,n3=n3,n2
if n1>n2:
    n1,n2=n2,n1
print(n1,n2,n3)

-------------------------------------------------------------------------------------------------------------------------------------------

#calculate pay based on number of hours worked
# hours   wage
#  <=40   17.75
#  >40 ~ <=50  1.5*17.75
#  >50 ~ <=60   2.0*17.75 
wage = 17.75
hours = eval(input("Enter hours worked during the week: "))
if hours<=40:
    pay = hours*wage
elif hours<=50:
    pay = 40*wage + (hours-40)*(1.5*wage)
elif hours<=60:
    pay = 40*wage + 10 * 1.5*wage + (hours-50)*(2*wage)
else:
    pay = 1000
    print("worked way too much, not allowed")
print("Pay is: " pay)

-------------------------------------------------------------------------------------------------------------------------------------------

#Repetition Statement: while loop, for loop, nested loop
#while loop for condition/sentinal controlled loop

#if you don't how how many iterations are needed use "while loop"

#for loop is used for counter controlled loop
#for loop: for i in range(5):    (i values are 0,1,2,3,4)
#for i in range (1,10):          (i values are 1,2,3,4,5,6,7,8,9)
#for i in range(1,10,2):         (i values are 1,3,5,7,9)
#Sample: Listing 5.3 P 138
#Sample: Exercise 5.29, 5.38
n = eval(input("Enter starting number: "))
print("Counting down from",n,"to 1")
for i in range(n,0,-1):
    print(i)

-------------------------------------------------------------------------------------------------------------------------------------------

# calculate pay for 4 weeks
wage = 17.75
total = 0
for i in range(1,5):
    hours = eval(input("Enter hours worked during week "+str(i)+": "))
    if hours<=40:
        pay = hours*wage
    elif hours<=50:
        pay = 40*wage + (hours-40)*(1.5*wage)
    elif hours<=60:
        pay = 40*wage + 10 * 1.5*wage + (hours-50)*(2*wage)
    else:
        pay =0
        print("worked way too much, not allowed")
    print("Week",i,"Pay is: $", pay)
    total+=pay
print("Total pay for 4 weeks is: $", total)

-------------------------------------------------------------------------------------------------------------------------------------------

#Functions
    
#define functions:
#def functionname(parameter list separated by commas):
#    statements
#Call function:
#    functionname(arguement list)  (handle the return data if any)
#Sample: write a function that sorts three numbers,
#then test this function in main with 5 sets of user data
def sort3(n1=1,n2=2,n3=3):    #(1,2,3 are default values, only used when arguements
are missing when calling the function)
    if n1>n2:
        n1,n2=n2,n1
    if n2>n3:
        n2,n3=n3,n2
    if n1>n2:
        n1,n2=n2,n1
    return n1,n2,n3
def main():
    print(sort3())   # call function with no arguement, default values will apply
    for i in range(5):
        num1,num2,num3 = eval(input("Enter 3 numbers separated by commas: "))
        x,y,z=sort3(num1,num2,num3)  # print(sort3(num1,num2,num3))
        print(x,y,z)
main()

-------------------------------------------------------------------------------------------------------------------------------------------

#calculate weekly pay for unknow number of weeks
def calculatepay(hours):
    wage = 17.75
    if hours<=40:
        pay = hours*wage
    elif hours<=50:
        pay = 40*wage + (hours-40)*(1.5*wage)
    elif hours<=60:
        pay = 40*wage + 10 * 1.5*wage + (hours-50)*(2*wage)
    else:
        pay =0
        print("worked way too much, not allowed")
    return pay
def main():
    total =0
    hours = eval(input("Enter hours worked during the week (-1 to quit): "))
    while hours>0:
        weekpay = calculatepay(hours)
        print("Pay for the week is: $", weekpay)
        total+=weekpay
        hours = eval(input("Enter hours worked during the week (-1 to quit): "))
    print("Total pay for these weeks is: $", total) 
main()

-------------------------------------------------------------------------------------------------------------------------------------------

---- #Sample Problem 1 ----
n = eval(input("Enter the number of student: "))
total = 0
highest = 0
passCount =0
for i in range(n):
    score = eval(input("Enter student score: "))
    total+=score
    if score > highest:
        highest = score
    if score >=70:
        passCount+=1
if n>0:
    avg = total/n
else:
    print("No score entered")
print("Total score:", total,
      "    Average score:", format(avg,".2f"),
      "    Highest score:", highest)
print("Number of students passed:", passCount, "out of", n)

-------------------------------------------------------------------------------------------------------------------------------------------

#Sample Problem 2
def getBMI(wt, ht):
    bmi = (wt*703)/(ht*ht)
    return bmi

#Option 2
def getStatus(bmi):
    if bmi<18.5:
        status = "Underweight"
    elif bmi<25:
        status = "Normal"
    elif bmi<30:
        status = "Overweight"
    else:
        status = "Obese"
    return status

#Option 3
def getBMIStatus(wt, ht):
    bmi = (wt*703)/(ht*ht)
    if bmi<18.5:
        status = "Underweight"
    elif bmi<25:
        status = "Normal"
    elif bmi<30:
        status = "Overweight"
    else:
        status = "Obese"
    return bmi, status
def main():
    height = eval(input("Enter your height: "))
    print("Your BMI Chart: \nHeight : ", height, "inches")
    print("Weight ", "      BMI")
    for weight in range(100, 201, 10):
        bmi = getBMI(weight, height)
        #Chanllenge option1 if...elif.. structure to get status
        
        print(weight, format(bmi, "15.1f"))
        #Challenge option2
        #status = getStatus(bmi)
        #Challenge option3
        #bmi, status = getBMIStatus(weight, height)
        
        #print(weight, format(bmi, "15.1f"), status)
main()
