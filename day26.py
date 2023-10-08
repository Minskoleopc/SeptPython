
# single inheritance
class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln
    def displayName(self):
        print(self.firstName+ self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl

    def displaySalary(self):
        print(self.salary)

amolT = Teacher("amol","rao",1000)
print(amolT.salary)
print(amolT.firstName)
print(amolT.lastName)
amolT.displayName()
amolT.displaySalary()


# multi-level


class GrandFather:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    def displayGname(self):
        print(self.firstName + self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fName = ffn

    def displayFanme(self):
        print(self.fName + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname  = ssn
    def displaySname(self):
        print(self.sname + self.lastName)

chinmay = Son("manohar","deshpande","shirsh","chinmay")
print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.fName)
print(chinmay.sname)

chinmay.displaySname()
chinmay.displayFanme()
chinmay.displayGname()

# program 3
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMName(self):
        print(self.firstName + self.lastName)

class SonM(Mother):

    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sname = sn

    def displaySname(self):
        print(self.sname + self.lastName)


class DaughterM(Mother):

    def __init__(self, fn, ln, dn):
        super().__init__(fn, ln)
        self.dname = dn

    def displayDname(self):
        print(self.dname + self.lastName)

chinmay = SonM("kanchan","deshpande","chinmay")
gauri = DaughterM("kanchan","deshpande","gauri")

chinmay.displaySname()
chinmay.displayMName()

gauri.displayMName()
gauri.displayDname()

# program 4


class FatherN:

    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print("Father method called")
        print(self.firstName + self.lastName)

class MotherN:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def displayName(self):
        print("Mother method called")
        print(self.firstName + self.lastName)

class SonN(MotherN,FatherN):
    def __init__(self,firstName, lastName,sname):
        super().__init__(firstName, lastName)
        self.sname = sname

    def displaySname(self):
        print(self.sname + self.lastName)

chinmayN = SonN("shirish","deshpande","chinmay")
chinmayN.displaySname()
chinmayN.displayName()







