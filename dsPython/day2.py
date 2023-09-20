import os ,Emp,sys
# count the number lines , words and characters in a file

# import os , sys
# f = open("myfile5.txt","w")
# while(str != "@"):
#     str = input("Enter the sentence ")
#     if str != "@":
#         f.write(str + "\n")
# f.close()

# str2 = input("Enter the fileName")
# if os.path.isfile(str2):
#     f = open(str2,'r')
# else:
#     print("coming out of loop")
#     sys.exit()
# #
# # for line in f:
# #     print(line)
#
# cw = 0
# cl = 0
# cc = 0
#
# for line in f:
#     cl = cl + 1
#     words = line.split(" ")
#     cw = cw + len(words)
#     cc = cc + len(line)
#
# print(cl)
# print(cw)
# print(cc)
# f.close()
#
# #["I","am","learning","javascript"]


# program 2
# f1 = open('minskoleLogo.jpg','rb')
# f2 = open('minskoleLogo2.jpg','wb')
# byte = f1.read()
# f2.write(byte)
# f1.close()
# f2.close()

# program 3
# with open('mySamlple.txt','a+') as f:
#     f.write("I am learning js"+"\n")
#     f.write("I am learning python"+"\n")
#     f.seek(0,0)
#     for line in f:
#         print(line)

with open('mySamlple.txt','r') as f:
    for line in f:
        print(line)

# program 4
# class Person:
#     def __init__(self,id,name,sal):
#         self.id = id
#         self.name = name
#         self.sal = sal
#
#     def display(self):
#         print("{}{}{}".format(self.id, self.name,self.sal))
#
# amol = Person(3234343243224,"chinmay",1654.878978789)
# amol.display()

#program 5

open("emp.dat")











































