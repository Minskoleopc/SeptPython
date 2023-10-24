
# count no of lines
# count no of characters
# count no of words
# import os , sys
# fname = input('Enter the name ')
# if os.path.isfile(fname):
#     f = open(fname,'r')
# else:
#     print(fname + "file not available")
#     sys.exit()
#
# cl = 0
# cw = 0
# cc = 0
#
# for line in f:
#     cl = cl + 1
#     cw = cw + len(line.split())
#     cc = cc + len(line)
#
# print(cl)
# print(cc)
# print(cw)

# program 2
# f1 = open('download.jpg','rb')
# f2 = open('new.jpg','wb')
# bytes = f1.read()
# f2.write(bytes)
# f2.close()
# f1.close()

# program 3

# with open('mytext5.txt','r') as f:
#     str = f.read()
#     print(str)

with open('mytext6.txt','w') as f2:
    str = input('Enter the sentence' + "\n")
    f2.write(str)













