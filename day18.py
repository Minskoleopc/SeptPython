

class Person:
    # properties
    first_Name = "amol"
    last_Name = "rao"
    age = 12
    rollNo = 44

    # attribute
    def walk(self):
        print("I am walking")
    def talk(self):
        print("I am talking")

amol = Person()
print(amol.first_Name)
print(amol.last_Name)
print(amol.age)
print(amol.rollNo)
amol.talk()
amol.walk()

chinmay = Person()
# retrive
print(chinmay.first_Name)
print(chinmay.last_Name)
print(chinmay.age)
print(chinmay.rollNo)

#update
chinmay.first_Name = "chinmay"
chinmay.last_Name = "deshpande"
chinmay.age = 12
chinmay.rollNo = 77
chinmay.city = "pune"

print(chinmay.first_Name)
print(chinmay.last_Name)
print(chinmay.age)
print(chinmay.rollNo)
print(chinmay.city)

del chinmay.city
chinmay.talk()
chinmay.walk()
#print(chinmay.city)


print(amol.first_Name)








