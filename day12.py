

last_name = "deshpande133"
q1 = last_name.isalpha()
print(q1)

last_name = "1231231284932849328493248932484893248930a"
q2 = last_name.isdigit()
print(q2)

last_name = "aaaasd123123123a@ssadfasfas"
q3 = last_name.isalnum()
print(q3)

#       firstName  lastName     phonenumber
info = ["chinmay","deshpande",7709192441,23,56]
print(info)
print(type(info))


# int
# float
# boolean
# List
# String
# dictionary


info2 = {
    # prop:value
    # key:value
    "first_Name":"chinmay",
    "last_Name":"deshpande",
    "age":28,
    "rollNo":56,
    "mobileNumber":7709192441,
    "age":45

}
print(info2)
# dictionary stores the value by index???  No
# dictionary stores duplicate key - pair ?? NO

# retrive
print(info2['first_Name'])
print(info2['age'])

#update
info2['first_Name'] = "tanmay"
print(info2)

#add
info2['city'] = "pune"
print(info2)

# delete
# info2.pop("age")
# print(info2)

print(len(info2))

# C  - create
# R  - retrive
# U  - update
# D  -  delete

vehicle = {
    "color":"red",
    "type":"sedane"
}

# retrive
print(vehicle['color'])

# update
vehicle['color'] = "blue"
print(vehicle)

# add
vehicle['reNo'] = 123
print(vehicle)

#delete
vehicle.pop('color')
print(vehicle)

q3 = len(vehicle)
print(q3)














