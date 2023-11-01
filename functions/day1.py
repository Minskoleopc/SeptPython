
# function day 1
# program 1
def addA(x,y):
    return x + y
q1 = addA(12,3)
print(q1)


# program 2
# function expressoion --- lamba functions
functionName = lambda parameter:expression
square = lambda x : x * x
a = square(5)
print(a)

# program 3
add = lambda x , y : x + y
b = add(2,2)
print(b)

# program 4
def addition(fn,x,y):
    #fn = lambda x , y : x + y
    c = fn(x,y)  # 15
    return c   # 15
d = addition(add,10,5)
print(d)


