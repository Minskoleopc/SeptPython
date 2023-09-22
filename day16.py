# tuple
# set , list , dict , tuple
# ordered
# indexed
# tuple -- add , change , update

#          0        1       2
tupleA = ("apple","mango","banana","apple")
print(tupleA)
print(type(tupleA))

#  accessing values from tuple
print(tupleA[0])
print(tupleA[1])
print(tupleA[2])

# updating values in list and tuple
flowers = ["lily","jasmine","rose","marrygold","lily"]
print(flowers)
flowers[0] = "lotus"
print(flowers)

# tupleB = (11,22,33)
# tupleB[0] = 111

# looping through tuple
#           0       1       2
tupleC = ("pune","wardha","nagpur")
cities = ["pune","mumbai","banglore"]
# using range()

for i in range(len(tupleC)):
    #print(i)
    print(tupleC[i])

# 2 way
for i in cities:
    print(i)

# types of tuple

tupleE = ("hindi","marathi","english")
tupleG = (11,22,33,44,55,66)
tupleF = (True , False , True ,False)
tupleB = ("chinmay","deshpande",7709192441)
tupleQ = tuple(["mango","banana","apple"])
tupleQ1 = tuple("banana")
tupleQ2 = tuple((34,55,66))
tupleQ3 = tuple({11,22,3,44,55})

print(tupleQ)
print(tupleQ1)
print(tupleQ2)
print(tupleQ3)


# program2
#          0  1  2  3  4 5
tupleD = (11,12,13,14,15,16)
#         -6 -5 -4 -3 -2 -1

print(tupleD)
print(tupleD[0])
print(tupleD[0:])
print(tupleD[1:5])
print(tupleD[-4])
print(tupleD[-4:])
print(tupleD[-4:5])
print(tupleD[1:-1])
print(tupleD[-1:-3])

#updating the tuple

e = (11,22,33)
# e[0] = 111
# print(e)

e = list(e)
print(e)
e[0] = 333
print(e)
e = tuple(e)
print(e)


# upacking of tuple
x = 10,
print(type(x))
fruits = ('apple',"mango","grapes","banana")

# (a ,b ,c) = fruits
# print(a)
# print(b)
# print(c)
(a,*b) = fruits
print(a)
print(b)

(a,*b,c) = fruits
print(a)
print(b)
print(c)








































