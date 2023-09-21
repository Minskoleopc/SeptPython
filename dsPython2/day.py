
# # program 1
# # opening the file for writing data
# f = open("myfile.txt","w")
# # enter the characters from the keyword
# str = input("enter the text")
# # writing the string into the file
# f.write(str)
# # closing the file
# f.close()
#
# # program 2
# f = open("nyfile.txt","r")
# str  = f.read()
# print(str)
# f.close()


# program 3
# f = open('myfile.txt','w')
# print('Enter the @ to exit')
# while(str != "@"):
#     str = input("Enter the name") # @
#     if str != "@":
#         f.write(str + "\n")
# f.close()

# f = open("myfile.txt","r")
# q1 = f.read()
# print(q1)
# f.close()

# program 4
# read , write
# f = open("myfile3.txt","a+")
# while(str != "@"):
#     str  = input("Enter the name")
#     if(str != "@"):
#         f.write(str + "\n")
# f.seek(0,0)
# str = f.read()
# print(str)
# f.close()

import os,sys
q1 = input("enter the filename")
if os.path.isfile(q1):
    f = open(q1,'r')
else:
    print(q1 + "does not exist")
    sys.exit()
str = f.read()
print(str)
f.close()















