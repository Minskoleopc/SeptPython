

# text
# img
# data


class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.salary = sal

    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)

#chinmay = Emp(1,"chinmay deshpande",1000)
#chinmay.display()
#obj   ------ file ----- dump ===> pickle
#file  ------ obj  ----- load ===> pickle

# import pickle
#
# # f = open('emp.dat','wb')
# # users  = int(input("Number of employee to be created")) #2
# # for x in range(users):
# #     name = input("Enter the name")
# #     id = input("Enter the id")
# #     salary = input("Enter the salary")
# #     e = Emp(name,id,salary)
# #     pickle.dump(e,f)
# # f.close()
#
#
# # reading
# f = open('emp.dat','rb')
# print("Employee details ......")
# while True:
#     try:
#         obj = pickle.load(f)
#         obj.display()
#     except Exception as e:
#         print(e)
#         break
# f.close()
#

import pickle
class Vehicle:
    def __init__(self,cl,type):
        self.color = cl
        self.type = type

    def displayTypeAndColor(self):
        print(self.type)
        print(self.color)

f = open("vehicle.dat","wb")
users = int(input("Enter the number of vehicles "))
for x in range(users):
    color = input("Enter the color ")
    type = input('Enter the type')
    e = Vehicle(color,type)
    pickle.dump(e,f)
f.close()

f = open('vehicle.dat','rb')
while True:
    try:
       obj = pickle.load(f)
       obj.displayTypeAndColor()
    except EOFError as e:
        print(e)
        break
f.close()







