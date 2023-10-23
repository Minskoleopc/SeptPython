# write
# f = open('text6.txt','w')
# str = input("Enter the name")
# f.write(str)
# f.close()

# read

# f2 = open('text6.txt','r')
# str = f2.read()
# print(str)
# f2.close()

# append
# f3 = open('text7.txt','a')
# print('Type @ to stop the writing')
# userInput = None
# while(userInput != '@'):
#     userInput = input("Enter the names ") #chinmay sarika poorva
#     if(userInput != '@'):
#         f3.write(userInput + "\n")
# f3.close()

# readLine by line
#
# f4 = open('text7.txt','r')
# listA = f4.readlines()
# print(listA)
# for item in listA:
#     print(item)
# f4.close()

# program 5
# r - read
# w - write
# a - append
# a+ - append + read
# f5 = open('text9.txt','a+')
# print('@ to stop the input')
# userInput = None
# while(userInput != '@'):
#     userInput = input('Enter the name')
#     if(userInput != '@'):
#         f5.write(userInput + "\n")
# f5.seek(0,0)
# str = f5.read()
# print(str)
# f5.close()

# program 6
# module , package , libraby
# program (class / functions) -----> modules
# packages -----> modules
# libraries -----> multiple packages
import os,sys
fname = input('Enter the fileName ')
if os.path.isfile(fname):
    f6 = open(fname,'r')
else:
    print(fname, 'does not exist')
    sys.exit()

strQ = f6.read()
print(strQ)
f6.close()




































