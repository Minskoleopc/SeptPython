

reclen = 10

with open('cities.bin','wb') as f:
    n = int(input("enter the numbers of cities?"))  # 4
    for i in range(n):
        str = input("Enter the city")  #pune
        ln = len(str) # 4
        str = str + (reclen - ln) * " "  #"pune      "
        str = str.encode()
        f.write(str)


# reclen = 10
# with open('cities.bin','rb') as f:
#     n = int(input('Enter the record you wish to read'))  #3
#     f.seek(reclen *(n-1))
#     str = f.read(reclen)
#     str = str.decode()
#     print(str)


# search for a particular city

# 10
# 60  -- 6 cities
# loop should run 6 times
# f.seek(0) ---- f.read(10) == userinput -----> break
# f.seek(10) --- f.read(10) == userinput ------> break
# f.seek(20) --- f.read(10) == userinput -----> break































