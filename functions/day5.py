# program 1
def myfunc():
    a = 1
    a = a + 1
    print(a) # 2
myfunc()
#print(a)

# program 2
b = 2
def func2():
    b = 3
    b = b  + 1
    print(b) # 4
func2()
print(b) # 2

# program 3
a = 3
def func3():
    global a
    a = 2
    print(a) # 2
print(a) # 3
func3()
print(a) # 2

# program 4
a = 10
def myfunction4():
    a = 56  # local
    x = globals()['a']
    print(x) # 10
    print(a) # 56
print(a) # 10
myfunction4()
print(a) # 10

# function -- lambda 
# list comprehension 
# **kwargs  , agrs*
# decorators 
# genrators
# local and global
# list tuple dictionary set  list

# 9 am 










