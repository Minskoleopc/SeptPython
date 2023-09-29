# program 1
# class Person:
#     firstname = "chinmay"
#     lastName = "deshpande"
#     adharNo = 123
#
#     def displayName(self):
#         print(self.firstname + self.lastName)
#
# # obj 1
# amol = Person()
# print(type(amol))
# print(amol.firstname)
# print(amol.lastName)
# print(amol.adharNo)
# amol.displayName()
#
# amol.firstname = "amolr"
# amol.lastName = "raor"
# amol.adharNo = 567
# amol.displayName()
#
# # obj 2
# chinmay = Person()
# print(chinmay.firstname)
# print(chinmay.lastName)
# print(chinmay.adharNo)
# chinmay.displayName()


# program 2
# using constructor

class Person:
    # class level
    country = "India"

    # constructor
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn
        self.lastName = ln
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

amol2 = Person("amol2","rao2",4562)
amol3 = Person("amol3","rao3",4563)
amol4 = Person("amol4","ra4",4564)

amol2.displayName()
amol3.displayName()
amol4.displayName()

print(amol2.country)
print(amol3.country)
print(amol4.country)

# program 3

class Person:
    # class level variable
    country = "india"

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    # instance method
    def updateFirstName(self,fn):
        self.firstName = fn

    def updateLastName(self,ln):
        self.lastName = ln

    @classmethod
    def changeCount(cls,cntName):
        cls.country = cntName

amol3 = Person("amko","rock")
print(amol3.firstName)
print(amol3.lastName)
print(amol3.country)
amol3.country = "nepal"
print(amol3.country)
amol3.updateFirstName("amolR")
print(amol3.firstName)


chinmay3 = Person("chinmay3","deshpande")
print(chinmay3.country)


Person.changeCount("china")
print(chinmay3.country)
chinmay3.country = "bharat"
print(chinmay3.country)






