import re
# program
q1 = "an apple a day keeps doctor away"
r = re.findall(r'\ba[\w]*',q1)
print(r)

# program 2
q2 = "an apple a ay keeps doctor away"
r = re.findall(r'\ba[\w]*',q1)
print(r)


# program 3
str = "The meeting will be conducted on 21st and 1st  31st of every month"
q3 = re.findall(r'\d[\w]*',str)
print(q3)

str = "The meeting will be conducted on 21st and 1st  31st of every month"
q4 = re.findall(r'\d\d[\w]*',str)
print(q4)


# program 4
str2 = "one two three 4 5 6 7 8 nine ten 7777 88888 99999"
q5 = re.findall(r'\d[\d]*',str2)
print(q5)

# program 5
str2 = "one two three 4 5 6 7 8 nine ten 7777 88888 99999 five four seven"
q6 = re.findall(r'\b\w\w\w\b',str2)
q7 = re.findall(r'\b\w{3}\b',str2)
q8 = re.findall(r'\b\w{4,}\b',str2)
q9 = re.findall(r'\b\w{4,5}\b',str2)
print(q6)
print(q7)
print(q8)
print(q9)

# program 6

q10 = "9766909110 8888 8888537485 7709192441 9860106021 6666"
q11 = re.findall(r'\d{10}',q10)
print(q11)

# program 7
q12 = "two three four five six seven eight nine ten"
q13 = re.findall(r't[\w]*\Z',q12)
print(q13)

q13 = re.findall(r'\At[\w]*',q12)
print(q13)

#program 8

q15 = "mayuri rao: 9766909110"
q16 = re.search(r'\D+[a-z]',q15)
print(q16.group())

# program  9

str = "anil akhil ankur arun arti abhijit anand a8new"
q17 = re.findall(r'an[\w]*',str)
q18 = re.findall(r'a[nk][\w]*',str)
q19 = re.findall(r'a[a-z][\w]*',str)

print(q17)
print(q18)
print(q19)

#program 10
str = 'vijay  20 07-11-1989 ram 11 17-10-1990 chinmay 34 07-11-2008 kajal 26 07-11-89'
q20 = re.findall(r'\d{2}-\d{2}-\d{2,4}',str)
print(q20)

# program 11
str10 = "chinmay deshpande"
q21 = re.search(r'^ch',str10)
print("starts with "+q21.group())


str10 = "chinmay deshpande"
q21 = re.search(r'de$',str10)
print("ends with "+q21.group())

str10 = "chinmay deshpande"
q21 = re.search(r'De$',str10,re.IGNORECASE)
print("ends with "+q21.group())

str11 = "I am 10 marks I got 11 marks I got  99 marks"
q22 = re.findall(r'\d\d',str11)
print(q22)


# monday wednesday friday sat sun






















