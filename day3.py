# comparison operator
# entity < enity  =======> boolean  True or False
# < , > , <= , >= , != , ==
print( 3 > 2)
print(5 < 6)
print(2 != 3)
print(3 == 3)
print(3 >= 5)
print(3 <= 5)
print(3 >= 3)
print(3 <= 3)

# logical
#AND   - and

#True   and True  =====> True
#False  and True  =====> False
#True   and False =====> False
#False  and False =====> False

print(2 == 2 and 3 == 3)
print(2 == 3 and 3 == 3)
print(2 == 2 and 3 != 3)
print(2 != 2 and 3 != 3)

#OR  - or
#True   or True  =====> True
#False  or True  =====> True
#True   or False =====> True
#False  or False =====> False

print(4 == 4 or 5 == 5)
print(5 != 5 or 6 == 6)
print(5 == 5 or 6 != 6)
print(3 == 2 or 5 != 5)

# not

print(not 4 == 4)
print(not 3 != 3)

#Not  - not
#not False   =====> True
#not True    =====> False

# conditional statement
# one input and multiple outcomes

# numT > 0 and numT <= 5  -------> 5 % discount
# numT > 5 and numT <= 10 -------> 10 % discount
# numT > 10               -------> 20 % discount

#if(condition):
    # statement will run if condition is true
# program 2
numT = 17
if(numT > 0 and numT <=5):
    print('5 % discount')
if(numT > 5 and numT <= 10):
    print('10 % discount')
if(numT > 10):
    print('20 % discount')

# program 3
numT = 5

if(numT > 0 and numT <= 5):
    print('5 % discount')
elif(numT > 5 and numT <= 10):
    print('10 % discount')
elif(numT > 20):
    print('20 % discount')
else:
    print("Incoorect input")





























