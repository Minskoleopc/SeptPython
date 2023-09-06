
# append()
names = ["chinmay","sarika","poorva","smitesh"]
a1 = names.append("shivani")
print(names)
print(a1)

# copy()
cities = ["pune","mumbai","banglore", "kolkata"]
cities2 = cities
cities2[0] = "nagpur"
print(cities)
print(cities2)

# reverse()
fruits = ["apple","mango","banana"]
a2 = fruits.reverse()
print(a2)
print(fruits)

# remove() pop()
#             0          1          2      3
country  = ["india","bangladesh","japan","cuba"]
# a3 = country.remove("japan")
# print(country)
# print(a3)

a4 = country.pop()
print(country)
print(a4)

a5 = country.pop(1)
print(a5)

# clear()
state  = ["MH","RJ","MP","UP"]
state.clear()
print(state)


# count
#          0    1    2    3    4     5   6
state  = ["MH","RJ","MP","UP","MH","RJ","MH"]
a6 = state.count("MH")
print(a6)

#index()
a7 = state.index("MH",2)
print(a7)

listA = [11,22,33]
listB = [44,55,66]
#listA.extend(listB)
listB.extend(listA)
print(listB)


listE = ["deshpande","rao","sorte","ahmed"]
listE.sort()
print(listE)



















