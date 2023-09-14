

import os
import shutil

print(os.getcwd())
os.chdir('../')
print(os.getcwd())
os.chdir('C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\src\\src2')
print(os.getcwd())


#os.mkdir("src2a")
#os.rmdir("src2a")
# q1 = os.listdir("C:\\Users\\Lenovo\\PycharmProjects\\pythonProject1\\venv\src\\src2")
# print(q1)

# for x in range(7,12):
#     os.mkdir("sreenshot"+"-"+str(x))
for x in range(7,12):
    os.rmdir("sreenshot"+"-"+str(x))
