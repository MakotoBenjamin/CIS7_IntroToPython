def footToMeter(foot):
    meter = 0.305 * foot

    return (meter)

def meterToFoot(meter):
    foot = meter/0.305

    return (foot)

def main():
    print(format("Feet",'<10') + format("Meters", '<10') + format("|",'<5') + format("Meters", '<10') + format("Feet", '<10'))

    y = 20.0
    
    for x in range(1,11):
        print(format(float(x),'<9.2f'), format(footToMeter(x),'<9.3f'), format("|",'<5'), end = "")

        print(format(y,'<9.2f'),format(meterToFoot(y),'<9.3f'))

        if y % 10 == 0:
            y += 6
        else:
            y +=4
    
main()
