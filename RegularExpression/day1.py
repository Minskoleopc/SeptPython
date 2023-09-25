

# program 1
print(r"I am learning javascript \n and python")
import  re
program = re.compile(r'm\w\w') # [a-z A-Z 0-9]
str = "cat mat hat sat"
a = program.search(str)
print(a)
print(a.group())

# program 2
str = 'aat cat sun qop run'
a = re.search(r'm\w\w',str)
if a:
    print(a.group())
else:
    print("match not found")

# program 3
str = 'mat mad sun run match sad mak'
a2 = re.findall(r'm\w\w',str)
print(a2)
for item in a2:
    print(item)

#program 4
str = 'bat cat sun run match bad mak'
a3 = re.match(r'b\w\w',str)
if a3:
    print(a3.group())

#program 5
str  = 'This;isthe:"core"python\'sbook'
a3 = re.split(r'\W+',str)
print(a3)

# program 6
str = 'I am learning javascript'
a4 = re.sub(r'javascript','python',str)
print(a4)

# program 7

# A python program to create a regular expression to find words starting with
# str = "an apple a day keeps doctor away"
# result = re.findall(r'a[\w]*',str)  # \w[a-z A-Z 0-9]
# print(result)

# str = "an apple a day keeps doctor away"
# result = re.findall(r'\ba[\w]*',str)  # \w[a-z A-Z 0-9]
# print(result)

# program 8
str = "The meeting will be conducted on 1st and 21st of every month"
#'\w'  [a-z A-Z 0-9]
# '\d' [0-9]
# '\W' non - alphanumeric
#   D  non -numeric
result2 = re.findall(r'\d[\w]*',str)
print(result2)

result2 = re.findall(r'\d[\d]*',str)
print(result2)


# program 9
str = "one two three four five six seven eight nine ten"
#[three , seven , eight]
q2 = re.findall(r'\b\w{5}\b',str)
print(q2)

# program 10
# first occurence
str = "one two three four five six seven 8 9 10"
q2 = re.search(r'\b\w{5}\b',str)
print(q2.group())

#program 11
str = "one two three four five six seven 8 9 10"
q3 = re.findall(r'\b\w{4,}\b',str)
print(q3)

# program 12
str = "one two three four five six seven 8 9 10"
q4 = re.findall(r'\b\w{3,5}\b',str)
print(q4)

# program 13
str = "one two three four five six seven 8 9 10"
q4 = re.findall(r'\b\d{1,}\b',str)
print(q4)

# program 14
str4 = "one two three"
#'\A' --- start  of string
#'\Z' --- end  of string
print(re.findall(r'\Ao[\w]*',str4))
print(re.findall(r't[\w]*\Z',str4))



































