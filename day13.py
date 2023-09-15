
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


dictB =  {

    "firstName":"chinmay",
    "lastName":"deshpande",
    "age":11,
    "rollNo":45
}
for key in dictB:
    print(key,dictB[key])


vehicle = {
    "color":"red",
    "regNo":123
}

# vehicleB = vehicle
# vehicleB['color'] = "blue"
#
# print(vehicleB)
# print(vehicle)

#copy()
vehicleC = vehicle.copy()
print(vehicleC)
print(vehicle)
vehicleC['color'] = "purple"
print(vehicleC)
print(vehicle)



vehicle = {
    "color":"red",
    "regNo":123,
    "city":"pune"
}

#keys()
for x in vehicle.keys():
    print(x)

# values()
for x in vehicle.values():
    print(x)


# items()
for x,y in vehicle.items():
    print(x,y)


#clear()
vehicle.clear()
print(vehicle)


student = {
    "marks":[11,22,33,4],
    "school":"DPS",
    "language":"English"
}

# print(student)
# # popitem()
# student.popitem()
#
# #pop()
# student.pop("school")
# print(student)

student.update({"age":25})
print(student)

q1 = student.get("age")
print(q1)


























# dict copy
