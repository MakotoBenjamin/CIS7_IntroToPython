def counts(s, ch):
    
    characterCount = 0

    for i in range(0,len(s)):
        
        if ch == s[i]:
        
            characterCount += 1
    
    return characterCount

def main():
    
    #s, ch = input("Please enter a word followed by a character: ").split()
    
    s = "The quick brown fox jumps over the lazy dog."
    ch = 'o'

    characters = counts(s, ch)

    print("The character \"" + ch + "\" occured " + str(characters) + " times.")

main()
