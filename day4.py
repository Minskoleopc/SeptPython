

# one input and multiple outcome

# numT > 0 and numT <= 5 -------->   10 % discount
# numT > 5 and numT <= 5 -------->   20 % discount
# numT > 10              -------->   30 % discount

# if(condition):
#     pass
numT = 17
if(numT > 0 and numT <= 5):
    print("10 % discount")
if(numT > 5 and numT <= 10):
    print("20 % discount")
if(numT > 10):
    print("30 % discount")

# program 2
numT = -17
if(numT > 0 and numT <= 5):
    print("10 % discount")
elif(numT > 5 and numT <= 10):
    print("20 % discount")
elif(numT > 10):
    print("30 % discount")
else:
    print("incorrect input")

# program 3
marks = 55
# if(marks > 90):
#     print("Grade A")
# if(marks > 75):
#     print("Grade B")
# if(marks >65):
#     print("Grade C")

if(marks > 90):
    print("Grade A")
elif(marks > 75):
    print("Grade B")
elif(marks >65):
    print("Grade C")
else:
    print("Fail please try again")

# program 4
r = 10
q = 5

if r > q:
    print("r is greater")
else:
    print("q is greater")

x = 1000
y = 5000
z = 30000
# if (x > y and x > z):
#     print("x is greater")
# elif(y > x and y > z):
#     print("y is greater")
# else:
#     print("z is greater")

if(x > y):
    if(x > z):
        print("x is greater")
    else:
        print("z is greater")
elif(y > z):
    print("y is greater")
else:
    print("z is greater")


# program 5
g = 10
h = 5
if g > h:
    print("g i greater")
else:
    print("h is greater")

# Tenary operator
print("g is greater") if g > h else print("h is greater")

age  = 17
q1 = "can drive" if  age >= 18 else "cannot driver"
print(q1)

# 7 sept
# 7.5 / 7.5 k
# 12.5k / 12.5k
# 12.5k / 12.5K

#11 sept -- datascience  python
#11 Sept -- sql
# dict , tuple , set , list , numpy , string


































































