#
# # program 1
# # write
# f = open('rtext.txt','w')
# str = input("Enter the name")
# f.write(str + "\n")
# f.close()
#
# # program 2
# f = open('rtext.txt','r')
# str = f.read()
# print(str)
# f.close()
#
# # program 3
# f = open('rtext.txt','a+')
# str = input("Enter the text")
# f.write(str + "\n")
# f.close()
#
# # program 4
# with open('rtext.txt','r') as f:
#     str = f.read()
#     print(str)
#
# with open('rtext.txt','w') as f:
#     str = input("Please enter the text")
#     f.write(str)
#
# with open('rtext.txt','a+') as f:
#     str = input("Please enter the text")
#     f.write(str)
#
# # program 5
#
# print('please enter @ to exit')
# f2 = open('r1.text','a+')
# userinput = None
# while(userInput != '@'):
#     str = input("Enter the name")
#     if str != '@':
#         f2.write(str)
# f2.seek(0,0)
# str = f2.read()
# print(str)
# f2.close()
#
# import os , sys
# fname = input("please the the file name")
# if os.path.isfile(fname):
#     f3 = open(fname,'r')
# else:
#     print(fname + " does not exist")
#     sys.exit()
# str = f3.read()
# print(str)
# f3.close()
#
# f1 = open('new.jpg','rb')
# f2 = open('new2.jpg','wb')
# bytes = f1.read()
# f2.write(bytes)
# f1.close()
# f2.close()
#
# d = open('r1.text','r')
# listA = d.readlines()
# for item in listA:
#     print(item)
#
# # for line in listA:
# #     print(line)
#
# d.close()

"""
"i am learning js"      ----> ['i','am','learning',js]
"i am learning python"  ---->['i','am','learning','python']
"i am learning ruby"    ----> ['i','am','learning','ruby']

"""
#
# cc = 0
# cw = 0
# cl = 0
#
# f = open('mytext6.txt','r')
# for line in f:
#     cl = cl + 1
#     cw = cw + len(line.split())
#     cc = cc +len(line)
#
# #print(cl)
# #print(cw)
# #print(cc)
# f.close()
#
























