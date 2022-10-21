'''
This stops at 2 because x is never able to reach the increment. It continues and go right back to the beginning of the code

x = 0
while x < 5:
    if x == 2:
        continue
    print(x)
    x += 1
'''

#This will skip 3 as intended because the increment comes before the "if", this allows the incrememnt to occur then check to see if the value is three. If the value is three you don't print and go back to the start of the loop.
i = 0
while i < 9:
    i += 1
    if i == 3:
        continue
    print(i)

  
'''
for i in range(1,5):
    if i == 2:
        continue
    print(i)
    '''
