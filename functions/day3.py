
# program 1
# positional arguments
def  additionA(x,y):
    return x + y
w = additionA(13,5)  # actual arguments
print(w)

# program 2
def additionB(x,y):
    return x + y
q1 = additionB(y = 12,x = 11)
print(q1)

# program 3 # Default values
def additionC(x = 10 , y=  2):
    return x + y
q3 = additionC()
print(q3)

# program 4
h = [11,22,33]
total = 0
for item in h:
    total = total + item
print(total)

# program 5
def additionE(*args):
   print(args)
   total = 0
   for item in args:
       total = total + item
   return total
print(additionE(12,2,3,4,5,6,7,8,3,4,5,66,7,8))

# program 6
def printInfo(**kwargs):
    print(kwargs)
    for k,y in kwargs.items():
        print(k,y)
printInfo(firstName="chinmay",lastName = "deshpande",rollNo = 45)


x = 10
print(x)
print(type(x))

y = 4,5
print(y)
print(type(y))

q1,q2 = y
print(q1)
print(q2)


# Functions
# local and global variable
# decorators
# recursive function
# generators

# regular expression
# Adv python and Django


# API / Graphl / Post ----- Git



