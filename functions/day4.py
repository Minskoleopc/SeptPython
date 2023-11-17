# # program 1
# def addTwo(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
#
# @addTwo
# def num():
#     return 10
#
# print(num())
#
# @addTwo
# def sub():
#     return 8 - 2
#
# print(sub())
#
#
# # program 2
# def decorTwo(fun):
#     def inner():
#         value = fun()
#         return value * 2
#     return inner
#
# @decorTwo
# def mul():
#     return 10
# print(mul())

# # program 3
# def calculate10Percentage(fun):
#     def inner():
#         return fun() * 0.10
#     return inner
#
# @calculate10Percentage
# def SalaryDiscount():
#     return 10000
#
# print(SalaryDiscount())

# program 4
# def decor(fun):
#     def inner():
#         val = fun()
#         return val + 2
#     return inner
#
# def decor2(fun):
#     def inner():
#         return fun() * 2
#     return inner
#
# @decor
# @decor2
# def num():
#     return 10
# print(num())

# program 5
for item in range(6):
    print(item)


# 0  1  2  3  4  5  6
def mygen(x,y):
    while x <= y:
      yield x   # 5 6 7 8 9 10
      x = x + 1
q1 = mygen(5,10)
print(q1)

# generator
# for item in q1:
#     print(item)
#
# q2 = next(q1)
# q3 = next(q1)
# q4 = next(q1)
# q5 = next(q1)
# q6 = next(q1)
# q7 = next(q1)

# print(q2)
# print(q3)
# print(q4)
# print(q5)
# print(q7)
while True:
    try:
        value = next(q1)
        print(value) # 5 # 6 # 7 # 8  #9 #10
    except StopIteration:
        # StopIteration is raised when the generator is exhausted
        break




def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
f =  mygen() # A B C

print(next(f))
print(next(f))
print(next(f))







