n = cube = 0

while cube < 12000:
    cube = n ** 3
    n += 1

print("Largest n value that is less than 1200 is:", round(cube ** (1/3)))
