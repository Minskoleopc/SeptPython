import os
reclen = 10
size = os.path.getsize("cities.bin")  # 30
n = int(size/reclen)  // 3
print("total number of records "+str(n))

with open('cities.bin','rb') as f:
    name = input("Enter the city ")  # "pune"
    name = name + (reclen- len(name))* " " # "pune        "
    name = name.encode()  # both are encoded
    position = 0
    found = False
    for x in range(n):
        f.seek(position) # 0
        str = f.read(10)
        if str == name:
            found = True
            break
        position = position + reclen
if not found:
    print("city not found")
else:
    print("city found")


#'pune'
#'pune         '





