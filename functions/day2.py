
# program1
def addition(x,y):
    return x + y

q1 = addition(13,5)
print(q1)

# lamda function
add = lambda x , y : x + y
q2 = add(23,4)
print(q2)

# program 2
lst = [1989,1990,1991,1992]
ages = []
# [34,33,32,31]
print(lst)

for item in lst:
    a = 2023 - item
    ages.append(a)
print(ages)

calculateAge = lambda  x :2023 - x
q3 = list(map(calculateAge,lst))
print(q3)

lstA  = [11,22,33,44,55,66]
q4 = list(map(lambda x:x+2,lstA))
print(q4)


# filter
marks = [11,22,33,44,55,22,33,44]
above40 = [] #[44,55,44]
for item in marks:
    if item > 40:
        above40.append(item)
print(above40)
q5 = list(filter(lambda  x : x > 40 ,marks))
print(q5)

# reduce
s = [11,22,33]
total = 0
for item in s:
    total = total + item
print(total)

import  functools
#from functools import reduce
print(functools.reduce(lambda acc,y:acc+y,s,5))












