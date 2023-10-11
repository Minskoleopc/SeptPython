
# program 1
class Duck:
    def talk(self):
        print("quack quack")

class Cat:
    def talk(self):
        print("meow meow")

def call_talk(obj):
    obj.talk()

a  = Cat()
b = Duck()
call_talk(a)
call_talk(b)


# duck = Duck()
# duck.talk()
# cat = Cat()
# cat.talk()

# program 2
class Dog:
    def bark(self):
        print("Bow Bow")

class Human:
    def talk(self):
        print("Hello hi ")

class Cat:
    def talk(self):
        print("meow meow")

def call_talk(obj):
    if(hasattr(obj,'talk')):
        obj.talk()
    elif(hasattr(obj,'bark')):
        obj.bark()
    else:
        print("wrong object pass")

a1 = Dog()

# b1 = Cat()
# c1 = Human()
call_talk(a1)
# call_talk(b1)
# call_talk(c1)

# program 3
print(10 + 15) # 25
print("hello "+ "world") # "helloworl"
print([11,22,23]+[44,55,66]) # [11,22,33,44,55,66]


# operator overloading
class Bookx():
    def __init__(self,x):
        self.pages = x
class Booky():
    def __init__(self,y):
        self.pages = y

b1 = Bookx(12)
b2 = Booky(23)
#print(b1 + b2)
print(b1.pages + b1.pages)





















