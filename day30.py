
# program 1
# operator overloading
# 3 examples

print(2  +  3)   # 5
print("hello"+ "amol") # "hello amol"
print([11,22,33]+ [44,55,66]) # [11,22,33,44,55,66]

class Bookx:
    def __init__(self,x):
        self.pages = x

class Booky:
    def __init__(self,x):
        self.pages = x

ramayan = Bookx(23)
mahabharat = Booky(34)
#print(ramayan + mahabharat)
print(ramayan.pages+mahabharat.pages)






class Bookx:
    def __init__(self,x):
        self.pages = x
    def __add__(self, other):
        return self.pages + other.pages

class Booky:
    def __init__(self,x):
        self.pages = x

ramayan = Bookx(23)
mahabharat = Booky(34)
print(ramayan + mahabharat)


# program 2
class Bookx:
    def __init__(self,x):
        self.pages = x
    def __add__(self, other):
        return self.pages + other.pages
    def __gt__(self, other):
        return self.pages > other.pages

class Booky:
    def __init__(self,x):
        self.pages = x

ramayan = Bookx(230)
mahabharat = Booky(340)
print(ramayan.pages > mahabharat.pages)
print( ramayan > mahabharat)

# program 3

class Employee:
    def __init__(self,name,pds):
        self.name = name
        self.pds = pds
    def __mul__(self, other):
        return self.pds * other.days

class Attendance:
    def __init__(self,days):
        self.days =  days

amol = Employee("amol rao",100)
amola = Attendance(25)
print(amol.pds * amola.days)
print(amol * amola)

# overloading

class Calculator:

    # def addition(self,x,y):
    #     print(self.x + self.y)
    #
    # def addition(self,x,y,z):
    #     print(self.x + self.y+self.z)
    #
    # def addition(self,x,y,z,a):
    #     print(self.x + self.y+self.z+self.a)

    def addition(self,x=None, y = None , z = None , a = None):
        if(x != None and y  != None and z != None and a != None):
            print(x+y+z+a)
        elif(x != None and y  != None and z != None):
            print(x+y+z)
        elif (x != None and y != None):
            print(x + y)

a = Calculator()
a.addition(13,44)
a.addition(13,44,66)
a.addition(13,44,66,4)

# overriding
# same method , same signature , different class has a relationship
class WorldBank:
    def save(self):
        print("I am save from worldbank 7%")

    def loan(self):
        print("I am loan from worldbank 9 %")

class SBI(WorldBank):
    def save(self):
        print("I am save from SBI 17%")
        super().save()

    def loan(self):
        print("I am loan from SBI 19 %")
        super().loan()

class PNB(WorldBank):
    pass

a = SBI()
a.save()
a.loan()
# b = PNB()
# b.loan()
# b.save()

# Duck typing
# Operator overloading
# Method overloading
# Method overriding

# 7-8 --- abtraction and interface
# function ----> regular expression , filehandling , exception handling























