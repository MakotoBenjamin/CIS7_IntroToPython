kilos = 1
    
print(format("Kilograms",'<9s'),format("Pounds",'>9s'))

while kilos < 200:
    lbs = kilos * 2.2
    
    print(format(kilos,'<9d'),format(lbs,'9.1f'))
    kilos += 2
    
