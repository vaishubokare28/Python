'''File Handling

Operatons of file handling
1. opening a file
2. reading data from file - r
3. writing data to a file - w
4. closing a file
'''

''' 1. opening a file
open(filename,mode)'''

# f=open("C:\Users\vaish\OneDrive\Desktop\vs code\PYTHON\FileHandling.py\demo1.txt","r")
# data=f.read()
# print(data)


#file read 3 ways
#1. normal way
f=open("demo1.txt",'r')
data=f.read()
print(data)

# fs=open("C:\Users\vaish\OneDrive\Desktop\vs code\PYTHON\FileHandling.py\demo1.txt",'r')
# for data in fs:
#  print(data)


#2. try and except block

#3. with open 
with open("demo2.txt","r") as f:
  d=f.read()
  print(d)

