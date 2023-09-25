
#        0  1  2  3
listA = [11,22,33,44]
print(listA[0])
print(listA[1])
print(listA[2])
print(listA[2])

tupleA = (11,22,33,44)
print(tupleA[0])
print(tupleA[1])
print(tupleA[2])
print(tupleA[3])

tupleA = 11,22
print(type(tupleA))

tupleA = tuple([11,22,33,44,55])
print(type(tupleA))

# difference between list and tuple
# add , update , delete
#           0         1        2        3
names = ["chinmay","sarika","poorva","ram"]
print(names[0])
names[0] = "tanmay"
print(names)

#tuple
# can not add value , update value or delete
#           0         1        2         3
names = ("chinmay","sarika","poorva","sanchita")
#names[0] = "tanmay"

# add
fruits = ("apple","mango","banana")
fruits = list(fruits)
#print(type(fruits))
fruits.append("chikoo")
print(fruits)
fruits = tuple(fruits)
print(fruits)

# update
vegetables = ("cabbage","tomato","potato")
vegetables = list(vegetables)
vegetables[0] = "cauliflower"
print(vegetables)
vegetables = tuple(vegetables)
print(vegetables)

# delete
flowers = ("lily","rose","jasmine","lotus")
print(flowers)
flowers = list(flowers)
flowers.pop(2)
print(flowers)
flowers  = tuple(flowers)
print(flowers)

# retrive
animals = ("tiger","lion","rabbit")
# print(animals[0])
# print(animals[1])
# print(animals[2])

# for loop
# using range

for x in range(3):
    #print(x)
    print(animals[x])
# without range
for item in animals:
    print(item)

# unpacking
cities = ('pune',"banglore" ,"kolkata","wardha")
#a,b,c = cities
#a,*b  = cities
a,*b,c = cities
print(a)
print(b)
print(c)

# methods
g = (11,22,33,11,22,33,11)
q1 = g.index(11)
print(q1)
q2 = g.count(11)
print(q2)

# dictionary , set , tuple , list
# conditional
# loops
# oops





#join operation on tuple
q = (11,22,33)
q2 = (44,55,66)

print(q + q2)
print(q * 2)
















