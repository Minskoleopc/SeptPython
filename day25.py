# program 1
class Student:
    def setFullName(self, fn):
        self.fullName = fn
    def getFullName(self):
        return self.fullName
    def setAge(self, ag):
        self.age = ag
    def getAge(self):
        return self.age
    def setAdharNo(self, no):
        self.adharNo = no
    def getAdharNo(self):
        return self.adharNo

class Teacher(Student):
    def setSalary(self,sl):
        self.salary = sl
    def getSalary(self):
        return self.salary

amol = Teacher()

amol.setFullName("amol rao")
amol.setAge(12)
amol.setAdharNo(4324)
amol.setSalary(1244)

print(amol.getAge())
print(amol.getFullName())
print(amol.getAdharNo())
print(amol.getSalary())

# child reference variable  parent properties and method access because of interitance
# program 2

# inheritance with constructor

class Person:

    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Professfor(Person):
    pass

sachin = Professfor("sachin","tendulkar")
print(sachin.firstName)
print(sachin.lastName)
sachin.displayName()

# program 3
class PersonB:
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class ProfessforB(PersonB):
    salary = 1000
    def displaySalay(self):
        print(self.salary)


sarika = ProfessforB("sarika","pansare")
print(sarika.firstName)
print(sarika.lastName)
print(sarika.salary)
sarika.displaySalay()
sarika.displayName()

# program 4
# parent contructor or child is also having constructor


















