import os
# program 1
# reclen = 20
# with open('cities.bin','wb') as f:
#     # writing the data into the file
#     n = int(input("How many entries ??"))
#     for x in range(n):
#         cityName = input('Enter the city name: ') #"nagpur"
#         ln = len(cityName) # 6
#         cityName = cityName + (reclen - ln)* " "
#         cityName = cityName.encode()
#         f.write(cityName)

# A python program to randomly access a record number

reclen = 20
with open('cities.bin','rb') as f:
    n = int(input("Enter a record number: ")) # 1
    # moving to that location
    f.seek(reclen * (n-1)) # 0
    str = f.read(reclen)  # 0-19 // 20 bytes
    print(str.decode())


# program 3
# A python program to search for for a city name in the file and display the record number which contain the city name

# number of 4
# size  = 80

reclen = 20
sizee = os.path.getsize('cities.bin')
numberOfrecords = int(sizee/ reclen)

# program 3
with open('ciites.bin','rb') as f:
    name = input("enter the cityname ")
    name  = name.encode()
    position = 0
    found = False
    for i  in range(numberOfrecords):
        f.seek(position) #20
        str = f.read(20)
        if name in str:
            print("record found at ",(i+1))
            found = True
        position = position + 20
    if not Found:
        print('city not found')















































