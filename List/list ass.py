# 1) create a list containing the names of five different fruites
l1=["apple","mango","orange","grapes"]

# 2)Add a new fruit to the list at end.
l1.append("banana")
print(l1)

# 3) Remove one fruit from index number 2
l1.pop(2)
print(l1)

# 4) Access and print the third fruit in the list.
print(l1[3])

# 5) Create a tuple containing three different colors.
t5=("black","red","purple")

# 6) Convert the tuple into list
a=list(t5)
print(a)

# 7) Add all elements from tuple to list
c=("riya","priya","siya")
t=[]
t.extend(c)
print(t)

# 8) Check length of list and tuple
print(len(t5))

# 9)check size of list and tuple
print(getsizeof(t))  
print(id(t))

print(getsizeof(c))  
print(id(c))

# 10) check memory location of list and tuple
print(id(t))
print(id(c))
