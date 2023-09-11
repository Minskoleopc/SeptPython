
# capitalize
first_name = "chinmay"
a1 = first_name.capitalize()
print(a1)

# lower()

last_Name = "DESHPANDE"
a2 = last_Name.lower()
print(a2)

# upper()

middle_name = "shirish"
a3 = middle_name.upper()
print(a3)

# strip()
city = " goa "
print(len(city))
a4 = city.strip()
print(a4)
print(len(a4))

# lstrip()
city2 = " goa "
print(len(city2))
a5 = city2.lstrip()
print(a5)
print(len(a5))
# rstrip()
city3 = "goa "
print(len(city3))
a6 = city3.rstrip()
print(a6)
print(len(a6))

# split()

email = "chinmaydeshpande010@gmail.com"
a7 = email.split("@")
a8 = email.split("a")
print(a7)
print(a8)

# ["chinmaydeshpande010","gmail.com"]
# ["chinm","ydeshp","nde010@gm","il.com"]
# .join()

info = ["chinmay","shirish","deshpande"]
a9 = "-".join(info)
print(a9)

#"chinmay-deshpande-7709192441".split("-") # ["chinmay","deshpande","7709192441"]
#"-".join(["chinmay","deshpande","7709192441"]) # "chinmay-deshpande-7709192441"

# startswith()
first_name2 = "ram"
a10 = first_name2.startswith("r")
a11 = first_name2.startswith("ra")
print(a10)
print(a11)

# endswith()

last_name = "dani"
a12 = last_name.endswith("i")
a13 = last_name.endswith("ni")
print(a12)

# find()
# 0  1  2  3  4  5
# j  a  i  p  u  r
# 0    1    2     3    4    5    6   7   8     9
# c    h    a     n    d    r    a   p   u     r
city5 = "jaipur"
city6 = "chandrapur"
a14 = city5.find("pu")
a15 = city6.find("a",4)
a16 = city6.find("a",1,3)
a17 = city6.find("A",1,3)
print(a14)
print(a15)
print(a16)
print(a17)
# index()

# 0 1 2  3 4  5 6
# k a n  p u  r a
city7 = "kanpura"
a18 = city7.index("a",0,7)
print(a18)

# count()
firstName3 = "chinmaya"
a19 = firstName3.count("a")
print(a19)

# isdigit()
mobileNumber = "7709192441"
a20 = mobileNumber.isdigit()
print(a20)

# isalpha()
country = "india1"
a21 = country.isalpha()
print(a21)

# isalnum()
mobileNumber = "4324"
print(mobileNumber.isalnum())




