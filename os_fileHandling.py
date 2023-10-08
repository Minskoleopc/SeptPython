#import os
# import shutil
#
# print(os.getcwd())
# os.chdir('../')
# print(os.getcwd())
# os.chdir('C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\src\\src2')
# print(os.getcwd())
import os

#os.mkdir("src2a")
#os.rmdir("src2a")
# q1 = os.listdir("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\src\\src2")
# print(q1)

# for x in range(7,12):
#     os.mkdir("sreenshot"+"-"+str(x))
# for x in range(7,12):
#     os.rmdir("sreenshot"+"-"+str(x))
# program 1
q1 = os.getcwd()
print(q1)

# program 2
# os.mkdir("mysub")
# print(q2)

# creating folder inside a folder
#os.mkdir('mysub/mysub2')

#os.mkdir('mysub2a')
#os.mkdir('mysub2a/mysub2b')

# program 3
# making folders inside a folder
#os.makedirs('subA/subB/Subc')

#program 4
# print(os.getcwd())
# os.chdir("subA/subB/Subc")
# print(os.getcwd())

# program5
# removing the directory
#os.rmdir('mysub')
#os.mkdir('ram')

#os.mkdir('ram/ram2')
#os.rmdir('ram/ram2')
#os.rmdir('ram')

# program 6
#os.makedirs('rule1/rule2/rule3')
#os.removedirs('rule1/rule2/rule3')

# program7
#os.rename("mysub2a","chinmay")

#program 8
q1 = os.getcwd()
print(q1)

for dirpath , dirnames , filenames in os.walk('.'):
    #print(dirpath)
    #print(dirnames)
    print(filenames)

# filehandling
#
# try:
#     # statements
# except Exception1:
#     # handler1
# except Exception2:
#    # handler2
# else:
#   print("i am into else")
# finally:
#    statements

# try ======> except ====>  except  =====>  else  ====> finally
# try:
#     date = eval(input("Enter the date :"))
# except NameError:
#     print("Printing the error")
# else:
#     print("you entered a date" ,date)


# program 3
# try:
#     name = input("Enter a file name")
#     f = open(name,'r')
# except IOError:
#     print("File not found")
# else:
#     str = f.readlines()
#     len(f.readlines())
#     print(str)
#     f.close()
# finally:
#     print(" i will run anyway")

# program 4
#
# listA = [11,22,33,44,55]
# listB = []
# listC= ["chinmay","sarika","poorva"]
# def avg(list):
#     total = 0
#     for x in list:
#         total = total + x
#     avg = total / len(list)
#     return total , avg
# try:
#     q1, q2 = avg(listC)
#     print(q1)
#     print(q2)
# except ZeroDivisionError:
#     print("please do not pass the empty list")
# except TypeError:
#     print("please provide the numbers")
#
# print("hello")

# program 5
#
# try:
#     x =  int(input('Enter the a number'))
#     y = 1 / x
#     print(y)
# finally:
#     print("We are not catching any exception")


# program 6
# try:
#     x  = int(input('Enter a number between 5 and 10: '))
#     assert  x >= 5 and x <= 10
#     print("pass")
# except AssertionError:
#     print('The condition is not fulfilled')
#
# try:
#     x  = int(input('Enter a number between 5 and 10: '))
#     assert  x >= 5 and x <= 10 , "your input is incorrect"
#     print("pass")
# except AssertionError as obj:
#     print('The condition is not fulfilled')
#     print(obj)













































