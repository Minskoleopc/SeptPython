
class Employee:
    def __init__(self,fullName,age,salary):
        self.fullName = fullName
        self.age = age
        self.salary = salary
    def displayInfo(self):
        print(self.fullName)
        print(self.age)
        print(self.salary)

class EmployeeInfo:
    @staticmethod
    def displayInfo(e):
        print(e.salary)
        print(e.fullName)
        print(e.age)

abhisha = Employee("abhisha","34",salary=1000)
abhisha.displayInfo()
EmployeeInfo.displayInfo(abhisha)

# program 3
class PersonR:
    # class variable
    country = "India"
    counter = 0
    # setting instance variable via object
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        PersonR.counter = PersonR.counter + 1

    def displayName(self):
        print(self.firstName+self.lastName)

    @classmethod
    def updateCountry(cls,cntry):
        cls.country = cntry

    @staticmethod
    def countObj():
        return PersonR.counter

sarika = PersonR("sarika","pansare")
print(sarika.firstName)
print(sarika.lastName)
PersonR.countObj()
PersonR.updateCountry("nepal")



