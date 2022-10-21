def premium(age):

    premium = ((age // 10) + 15) * 21.3

    return premium

def main():

    print(format("Age", '>3'), format("Insurance Premium", '>20'))

    for i in range(18, 79, 10):
        print(format(i,'>3d'), format("$"+str(format(premium(i),'.1f')),'>14s'))

main()
