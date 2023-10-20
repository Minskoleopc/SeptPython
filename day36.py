
# user defined exception
# Exception

# IDFC  ---- acc minimum limit ----- 10k
# HDFC  ---- acc minimum limit ----  25k

# class above25(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
# dict = {
#     "amol":26000,
#     "chinmay":25000,
#     "sarika":4000,
#     "poorva":3000
# }
#
# def check(dict):
#     for k,v in dict.items():
#         if v < 25000:
#             raise above25("Bal below expected 25k "+ k)
#
# try:
#     check(dict)
# except above25 as e:
#     print(e)


# program 1
# opening a file in write mode txt
# opening the file
# f = open("myfile5.txt",'w')
# # taking input from user
# str = input("Enter the names you want write on file")
# # writing on the file
# f.write(str)
# # closing the file
# f.close()


# program 2
# opening the file
# f = open('myfile5.txt','r')
# # reading the text from a file
# str2 = f.read()
# # print the content of file
# print(str2)
# # closing the file
# f.close()

# program 3
# f = open("myfile5.txt",'a')
# # taking input from user
# str = input("Enter the names you want write on file")
# # writing on the file
# f.write(str + "\n")
# # closing the file
# f.close()




