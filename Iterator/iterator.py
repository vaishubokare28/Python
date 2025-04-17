"""Iteratable-(for loop apply to a sequence) 
Iterator-(object) 
Iteration-(process) process of taking each item of something one after another """


l=[10,20,30,40,50]
for i in l:
    print(i)
print(dir(l))

list=[45,67,89,90]
iter_obj=iter(list)
print(iter_obj)
print(type(iter_obj))

l1=[23,64,78,98]
iter_obj=iter(l1)
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))
print(next(iter_obj))

l2=[12,25,62,77,91]
iter_obj=l2.__iter__()
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

name="kiranacademy"
iter_obj=name.__iter__()
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())
print(iter_obj.__next__())

