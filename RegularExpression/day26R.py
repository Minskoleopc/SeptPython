
# single

class Student:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    def displaySalary(self):
        print(self.salary)

amol = Teacher("amol",'rao',12000)
print(amol.firstName)
print(amol.lastName)
print(amol.salary)
amol.displayName()
amol.displaySalary()


# multi-level
class GrandFather:

    def __init__(self,fn,ln):
        self.firstName  = fn
        self.lastName = ln

    def displayGname(self):
        print(self.firstName+self.lastName)

class Father(GrandFather):
    def __init__(self,fn,ln,fname):
        super().__init__(fn,ln)
        self.fname = fname

    def displayFName(self):
        print(self.fname + self.lastName)

class Son(Father):
    def __init__(self,fn,ln,ffn,ssn):
        super().__init__(fn,ln,ffn)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastName)

amol = Son("amol","rao","dilip","ram")

print(amol.fname)
print(amol.sname)
print(amol.lastName)
print(amol.firstName)

amol.displayGname()
amol.displayFName()
amol.displaySname()


# hierarchical inheritance
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayMname(self):
        print(self.firstName + self.lastName)

class SonM(Mother):
    def __init__(self ,fn,ln,sname):
        super().__init__(fn,ln)
        self.sname = sname

    def displaySName(self):
        print(self.sname + self.lastName)


class DaughterM(Mother):
    def __init__(self, fn, ln, dname):
        super().__init__(fn, ln)
        self.dname = dname

    def displayDName(self):
        print(self.dname + self.lastName)

chinmay = SonM("kanchan","deshpande","chinmay")
gauri = DaughterM("kanchan","deshpande","gauri")

print(chinmay.firstName)
print(chinmay.lastName)
print(chinmay.sname)
chinmay.displayMname()
chinmay.displaySName()


# multiple inheritance
class FatherM():
    def __init__(self,fn,ln):
        self.firstName = fn
        self.lastName = ln

    def displayN(self):
        print("Father method called")
        print(self.firstName + self.lastName)

class MotherM():
    def __init__(self, fn, ln):
        self.firstName = fn
        self.lastName = ln

    def displayN(self):
        print("Mother method called")
        print(self.firstName + self.lastName)


class DaughterN(FatherM,MotherM):
    def __init__(self, fn, ln, dname):
        super().__init__(fn, ln)
        self.dname = dname

    def displayDName(self):
        print(self.dname + self.lastName)

gauri = DaughterN("shirish","deshpande","gauri")
gauri.displayN()
gauri.displayDName()



















