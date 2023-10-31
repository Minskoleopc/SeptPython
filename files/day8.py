

import os

reclen = 10

size = os.path.getsize('cities.bin')
n = int(size/10)
with open('cities.bin','r+b') as f:
    old = input("Please enter city to replace") # pune
    old = old.encode() # pune -- encided
    newc = input('please enter the new city') # ujjain
    newc = newc + (reclen - len(newc)) * ' ' # "ujjain    "
    newc = newc.encode()
    position = 0
    found = False
    for i in range(n):
        f.seek(position)
        strc = f.read(10)
        if old in strc:
            found = True
            f.seek(-10,1)
            f.write(newc)
        position = position + reclen

    if not found:
        print("city not found")






