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


































