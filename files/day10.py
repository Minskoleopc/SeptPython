import os
reclen = 10
size = os.path.getsize("cities.bin")
n = int(size/reclen)


f1 = open('cities.bin','rb')
f2 = open('file2.bin','wb')

city = input('Enter the city you wish to delete') # pune
city = city + (reclen - len(city)) * " "
city = city.encode()

for i in range(n):
    # 0 , 1, 2
    str = f1.read(reclen)
    if str != city:
        f2.write(str)

f1.close()
f2.close()

os.remove("cities.bin")
os.rename("file2.bin","cities.bin")





