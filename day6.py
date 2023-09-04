

x = 10
print(x)

# list
# list stores the value by index
#            0       1      2      3
names = ["chinmay","ram","sham","satish"]
print(names)
print(type(names))

#program 1 retrive
print(names[0])
print(names[1])
print(names[2])

# program 2 - update
names[2] = "sunny"
print(names)

# program -3 total numbers of element in list
cities = ["pune","mumbai","banglore","kolkata","chennai"]
a1 = len(cities)
print(a1)

# program 4 - loop
#           0
numbers = [22,33,44,55,66,77,88,99,100]
print(numbers[0])
print(numbers[1])
print(numbers[2])

# program 5 -  for using range() and basic for loop
# range(10) // 0 - 9
# range(1,10) // (1,9)'
# range(1,10,2) // 1,3,5,7,9

for x in range(10):
    print(x)

for x in range(1,10):
    print(x)

for x in range(1,10,2):
    print(x)

#           0       1       2        3        4
fruits = ["apple","mango","banana","grapes","chikoo"]
a1 = len(fruits)
print(a1)
for x in range(len(fruits)):
    #print(x)
    print(fruits[x])
    # x = 0
    # x = 1
    # x = 2
    # x = 3
    # x = 4
#          0        1        2         3
cities = ['pune',"mumbai","banglore","nagpur"]
for x in range(len(cities)):
    #print(x)
    print(cities[x])

#program 6
#               0          1        2        3
vegetables = ["potato","cabbage","ginger","tomato"]
for item in vegetables:
    print(item)

# program 7
marks = [11,22,33]
marks.append(44)
print(marks)
#  0  1  2  3
# [11,22,33,44]

marks.pop(2)
print(marks)






















