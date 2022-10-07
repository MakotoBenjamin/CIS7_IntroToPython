import calendar

month = eval(input("Enter a month: "))
year = eval(input("Enter a year: "))

if month > 12:
    print("!INVALID ENTRY!\n--- Exiting Program ---")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(calendar.month_name[month], year, "has 29 days.")
    else:
        print(calendar.month_name[month], year, "has 28 days.")
elif (month == 4 or month == 6 or month == 9 or month == 11):
    print(calendar.month_name[month], year, "has 30 days.")
else:
    print(calendar.month_name[month], year, "has 31 days.")
