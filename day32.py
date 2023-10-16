
# A decoratot is a function that accepts another function as parameter and return function
# program 1
# def decor(fun):
#     def inner():
#         value = fun()
#         return value + 2
#     return inner
#
# def num():
#     return 10
#
# q1 = decor(num)
# print(q1())


# program 2
# def decor(fun):
#     def inner():
#         value = fun() + 10
#         return value
#     return inner
#
# @decor
# def num():
#     return 10
# print(num())

# def addFive(fn):
#     def inner():
#         return fn()+5
#     return inner
#
# @addFive
# def numbers():
#     return 5
# print(numbers())

# program 3
# def decor(fun):
#     def inner():
#         return fun() + 2
#     return inner
#
# def decor1(fun):
#     def inner():
#         return  fun() * 2
#     return inner

# def num():
#     return 10
# q1 = decor(decor1(num))
# print(q1())


# @decor
# @decor1
# def num():
#     return 50
# print(num())
#
#
# # program 4
# def split_string(word):
#     def inner():
#         a = word().split(" ")
#         return a
#     return inner

# @split_string
# def word():
#     return "Octomber 2023"
#
#
# @split_string
# def date():
#     return  "10 November 1989"
# print(date())







