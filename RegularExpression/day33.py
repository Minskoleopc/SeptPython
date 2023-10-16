
from abc import  ABC ,abstractmethod
# interface
class worldBank(ABC):
    @abstractmethod
    def loan(self):
       pass

    @abstractmethod
    def save(self):
        pass

# wb = worldBank()
# can create the object of abstract class

class SBI(worldBank):
    def printBranch(self):
        print("Hello i am nagpur branch")

    def loan(self):
        print("i am loan from SBI")

    def save(self):
        print("I am save from SBI")

a = SBI()
a.save()
a.loan()


class Student(ABC):
    @abstractmethod
    def fullName(self):
        pass

    @abstractmethod
    def fullAddress(self):
        pass

    def displayCountry(self):
        print("India")

class Teacher(Student):
    def fullName(self):
        print("Chinmay Deshpande")

    def fullAddress(self):
        print("Pune")


class Professor(Student):
    def fullName(self):
        print("Vijeet Dani")

    def fullAddress(self):
        print("Nagpur")

a = Teacher()
b = Professor()

a.fullName()
a.fullAddress()

b.fullName()
b.fullAddress()

a.displayCountry()
b.displayCountry()

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.ra = radius

    def area(self):
        return 3.14 * self.ra  * self.ra

class Rectangle(Shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

recA = Rectangle(12,4)
circleA = Circle(5)

recA.area()
circleA.area()