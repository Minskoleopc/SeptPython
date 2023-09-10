
#           0        1      2
names = ["chinmay","ram","sham"]
print(names)
print(names[0])
# Object - properties and method

a1 = len(names)
print(a1)

# append()
fruits = ["apple","mango","banana"]
fruits.append("chikoo")
print(fruits)

#reverse()
fruits.reverse()
print(fruits)

# in
cities = ["pune","banglore","nagpur","mumbai"]
print("Pune" in cities)

# vegetables()
vegetables = ["carrot","cabbage","oninon","cauliflower","carrot"]
q1 = vegetables.index("carrot",2)
print(q1)

vegetables.clear()
print(vegetables)


numbers = [11,22,33]
numbersB = numbers

# numbersB[0] = 111
# print(numbers) # 111,22,33
# print(numbersB) #111,22,33

numbersC = numbersB.copy()
numbersC[1] = 44444

print(numbersC)
print(numbersB)

# names = ["shivani","ram","sham","laxman"]
# print("Shivani" in names)

flowers = ["rose","lily","jasmine","marygold"]
q2 = flowers.pop(2)
print(q2)
print(flowers)
#gym
# action ---- excercise
# return --- health

flowers.remove("lily")
print(flowers)

country = ["india","pakistan","srilanka","bangladesh"]
country.sort()
print(country)

n = [11,22,33]
m = [44,55,66,55,77,55]

# n.extend(m)
# print(n) # [11,22,33,44,55,66]
m.extend(n)
print(m)
m[2] = 333
print(m)

q2 = m.count(55)
print(q2)

m.insert(4,555)
print(m)

b = [11,22,33,44,55]
c = [66,77,88,99,00]


for x in range(10):
    print(x)

for x in range(1,10):
    print(x)

for x in range(3,31,3):
    print(x)

for x in range(len(b)):
    #print(x)
    print(b[x])

for item in c:
    print(item)

# for x in range(startPosition,endPosition(not included)):
#     print(x)

for x in range(5,10):
    print(x)

for x in range(5):
    print(x)

for x in range(2,21,3):
    print(x)


