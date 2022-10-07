subtotal, rate = eval(input("Enter the subtotal and a gratuity rate separated by a comma: "))

gratuity = round(subtotal * (rate / 100),2)
total = subtotal + gratuity

print("The gratuity is ", gratuity, " and the total is ", total)
