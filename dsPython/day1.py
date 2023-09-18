

# program 1
# opening the file
# f = open('myfile.txt','w')
# # user input from user
# str = input("Please enter the name")
# #writing into the file
# f.write(str)
# # closing the file
# f.close()


# program 2
#a)
# f = open('myfile.txt','r')
# str = f.read()
# print(str)
# f.close()
#

#b)
# f = open('myfile.txt','r')
# str = f.read(2)
# print(str)
# f.close()

#program 3 (append)
# f = open('myfile.txt','w')
# str = input('please enter your name')
# f.write(str)
# f.close()

# f = open('myfile.txt','a+')
# str = input('please enter your name')
# f.write(str)
# f.close()


#program 4
# f = open('mytxt2.txt','w')
# print('Enter the @ to end the input')
# while(str != '@'):
#     str = input("enter the name :") # @
#     if(str != '@'):
#         f.write(str + "\n")
# f.close()

# program 5
f = open('mytxt3.txt','a+')
print('Enter the @ to end the input')
while(str != '@'):
    str = input("Enter your name ??")
    if(str != '@'):
        f.write(str + "\n")
# starting reading from start of file
f.seek(0,0)
str2 = f.read()
print(str2)
f.close()

















