import random 

def sixtyFiveToNinety():
    
    generatedValue = 0
    count = 0

    print("Random numbers between 65 and 90 are:")

    for i in range(0,17):
        
        generatedValue = random.randint(65,90)
        
        if generatedValue % 2 != 0:
            count += 1

        print(generatedValue, end = " ")

    print("\nCout of odd numbers is:", count)


def findingVowel():
   
    print("Random upper case letters are:")
    
    randomUpper = '0'
    
    count = 0

    while randomUpper != 'A' and randomUpper != 'E' and randomUpper != 'I' and randomUpper != 'O' and randomUpper != 'U':
        
        randomUpper = chr(random.randint(65,90))

        print(randomUpper, end = " ")
        
        count += 1

    if count == 1:
        print("\nIt took", count, "try to get a vowel.")
    else:
        print("\nIt took", count, "tries to get a vowel.")

''' Testing to see if I'm converting correct ASCII characters:

    for i in range(65,91):
        character = chr(i)
    
        print(character, end = " ")
'''

sixtyFiveToNinety()

findingVowel()
