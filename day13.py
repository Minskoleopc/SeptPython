
#          0         1        2   3
list = ["chinmay","deshpande",23,45]

#retrive
print(list[0])
print(list[1])
# update
list[1] = "dani"
print(list)

list.append("pune")
print(list)

# delete
list.pop(3)
print(list)

#delete
list.remove("chinmay")
print(list)


dictA = {
    # property:value
    # key:value
    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":23,
    "rollNo":45
}

#print(dictA[0])
q1 = dictA['firstName']
print(q1)

# update
dictA['lastName'] = "dani"
print(dictA)

# add
dictA['age'] = 34
dictA['city'] = "pune"
print(dictA)

dictA.pop('city')
print(dictA)

#  C  R  U  D
# Create
# Retrive
# Update
# Delete

# type()
vehicle = {
    "color":"red",
    "type":"sedane"
}
print(vehicle)
print(type(vehicle))
print(len(vehicle))

# allows duplicate property ??
vehicle = {
    "color":"red",
    "type":"sedane",
    "color":"blue"
}
print(vehicle)

# loop
names = ["chinmay","sham","ram"]

for item in range(len(names)):
    print(names[item])

for item in names:
    print(item)


dictB = {
    "rule":1,
    "rule1":2,
    "rule2":3
}

for key in dictB:
    print(key,dictB[key])

















# dict copy
