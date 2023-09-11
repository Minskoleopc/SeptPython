
# capitalize
first_Name = "chinmay"
q1 = first_Name.capitalize()
print(q1)

# lower()

city = "PUNE"
q2 = city.lower()
print(q2)

# upper()
city2 = "nagpur"
q3 = city2.upper()
print(q3)

# strip()

city3 = " Goa "
q4 = len(city2)
print(q4)
q5 = city3.strip()
print(len(q5))
print(q5)

q6 = city3.lstrip()
print(len(q6))

q7 = city3.rstrip()

print(q7)
print(len(q7))


# split()
info = "chinmay deshpande 7709192441"
q8 = info.split(" ")
print(q8)

# .join()
names = ["chinmay","shirish","ram","satish"]
q9= "@".join(names)
print(q9)

#["chinmay" ,"deshpand"] ====> "chinmay deshpande"
#"chinmay deshpabde"    ====> ["chinmay","deshpande"]

info2 = "I am learning javascript"
q10 = info2.replace("javascript","python")
print(q10)


info3 = "mayuri katwe"
q11 = info3.startswith("m")
q12 = info3.startswith("may")
q13 = info3.endswith("e")
q14 = info3.endswith("We")
print(q11)
print(q12)
print(q13)
print(q14)

# find()

# index()

# count()

# isdigit()

# isalpha()

# isalnum()



