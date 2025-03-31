# # w- used to create a file and add data in it

# # fs=open("first.txt","w")
# # fs.write("Higher Order function")

# fs=open("second.txt","w")
# fs.write("Python is adynamic language")



# #a - append
# fs=open("second.txt","a")
# fs.write(". Python is interpreter language")



# #x mode- exclusion creation mode
# #if the file already exists , raise FileExitsError

# fs=open("second.txt","x")
# fs.write("hello") 



# #rb - read binary
# with open("second.txt","rb") as f:
#     print(f.mode)
#     print(f.name)
#     print(f.closed)

# f.closed
# print(f.closed)



# #r+ read and write mode
# # opens the file for both reading and writing
# # file must exist 
# with open ("demo3.txt","r+") as f:
#     content=f.read()
#     print(content)
#     f.write("functional programing")



#w+ write and read mode
# opens the file for writing and reading
#runcates the file if it exists, creates a new file if it doesn't
with open("file1.txt","w+") as f:
    f.write("lambda function")
    f.seek(0)
    data=f.read()
    print(data)