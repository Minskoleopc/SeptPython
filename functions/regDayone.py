# regular expression
#"I am chinmay deshpande and my mobile number is + 91 7709192441"
#"I am poorva vyas and my mobile number is + 91 9766909110"

#  "\d" -------   0 to 9
#  "\D" ------    any non - digit
#  "\w" ------    (A to Z , a to z , 0 - 9)
#  "\W" ------     Reresents non - alphanumeric

import re

sun = "sun mop run man mom"
q = re.search(r'm\w\w',sun)
# print(q.group())
if q:
    print(q.group())
else:
    print("Not found")


# program 2
str2 =  "cat rat mat sat sun ban can"
q2 = re.search(r'\wat',str2)
if q2:
    print(q2.group())
else:
    print('not found')


# program 3
# findall
str3 =  "cat rat mat sat sun ban can"
q3 = re.findall(r'\wa\w',str3)
print(q3)

#program 4
str4 = "mice rice choice ice mice"
q4 = re.findall(r'\Dice',str4)
print(q4)

# program 5
str5 = "sat man can mat hat chat sat wat"
q5 = re.match(r'm\w\w',str5)
print(q5)
if q5:
    print(q5.group())
else:
    print('not found')

# program 6
# non - alphanumeric
str6  = "This is core java class and i am learning same"
q6 = re.split(r'\W',str6)
print(q6)

# program 7

str7 = "I am learning python"
str = re.sub(r'\wython',"javascript",str7)
print(str)












