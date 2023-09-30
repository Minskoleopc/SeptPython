# program 1
# class Student:
#     def __init__(self):
#         self.name = "ram"
#         self.age = 20
#         self.marks = 200
#
#     def talk(self):
#         print("I am ", self.name)
#         print("I am",self.age,"years old")
#         print("I got ",self.marks)
#
# amol = Student()
# print(amol.name)
# print(amol.age)
# print(amol.marks)
#
# chinmay = Student()
# print(chinmay.name)
# print(chinmay.age)
# print(chinmay.marks)
#
# # updating value outside the class
# chinmay.name = "chinmay deshpande"
# print(chinmay.name)

# program 2

class Student:

    def __init__(self,name ,age ,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def talk(self):
        print("I am ", self.name)
        print("I am",self.age,"years old")
        print("I got ",self.marks,"marks")

amol2 = Student("amol rao",33,55)
chinmay2 = Student("chinmay deshpande",32,56)
amol2.talk()
chinmay2.talk()


# prorgram 3
# instance  and class variable


class Person:
    # class variable
    country = "india"

    def __init__(self,fn,ln,age):
        self.firstName = fn
        self.lastName = ln
        self.age = age

    # instance method (to retrive or update or add instance variable)

    # instance method to update firstName
    def updateFirstName(self,fn):
        self.firstName = fn

    # instance to add city propertu
    def addCity(self,cy):
        self.city = cy

    # instance method to retrive age
    def retriveAge(self):
        return self.age

    @classmethod
    def updateCountry(cls,cnty):
        Person.country = cnty


Person.updateCountry("bharat")
amol3 = Person("amol","rao",45)
print(amol3.firstName)
print(amol3.lastName)
print(amol3.age)
print(amol3.country)
amol3.country = "nepal"
print(amol3.country)

amol4 = Person("amol","rao",45)
print(amol4.country)
amol4.country = "srilanka"

amol5 = Person("amol5","rao5","66")
Person.updateCountry("pakistan")
amol5.country = "japan"
print(amol5.country)

amol6 = Person("amol5","rao5","66")
print(amol6.country)








