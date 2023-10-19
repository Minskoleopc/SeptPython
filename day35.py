# program 1

# logical error

# compile time error

# run time error
# try:
#     q1 = int(input("Enter the number one"))
#     q2 = int(input("Enter the number two"))
#     print(q1/q2)
#     lst = [11,22,33]
#     print(lst[2])
#     print(q3)
#
# except ZeroDivisionError as e:
#     print(e)
#     print("please input correct data")
# except IndexError as e:
#     print(e)
#     print("not so many elements available")
# except Exception as e:
#     print(e)
#     print("Error occured")


# try ------- except  ------- else -------- finally

# A single try block can be followed by several except block
# Multiple except blocks can manage multiple exceptions
# We cannot write except block without a try block
# We can write a try block with except block
# Else block and finally block are optional
# When there is no exception raised , else block will be executed
# Finally block is always executed

# program 2


# try:
#     q1 = int(input("Enter the number one"))
#     q2 = int(input("Enter the number two"))
#     print(q1 / q2)
# except Exception as e:
#     print(e)
#     print("please enter correct input")
# else:
#     print("I will executed when no exception is raised")

# program 3
# print("hello")
# try:
#     q1 = int(input("Enter the number one"))
#     q2 = int(input("Enter the number two"))
#     print(q1 / q2)
# finally:
#     print("We are not catching any exception")
# print("bye")
# try:
#     q1 = int(input("Enter the number one"))
#     q2 = int(input("Enter the number two"))
#     print(q1 / q2)
# except Exception as e:
#     print(e)
#     print("Please enter correct input")
# else:
#     print("Calculation was successful")
# finally:
#     print("I will executed anyway")

# program 4

# try:
#     x = int(input("please enter a  input"))
#     assert  x >= 5 and x <= 10
#     print("The number entered: ",x)
# except AssertionError:
#     print("This condition is not fullfiled")

try:
    x = int(input("please enter a  input"))
    assert  x >= 5 and x <= 10 , "The number was not in range"
    print("The number entered: ",x)
except AssertionError as e:
    print("This condition is not fullfiled")
    print(e)












