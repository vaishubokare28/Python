''' primitive datatype-
int, float, complex,boolean , string 

non primitive(collection dt)-
lis, set,tuple,dic 




List-
1. comma sept values within []

2. stores heterogenous elements (different datatype)

3. ordered - indexing

4. mutable - changable (insert,update,delete) '''



'''How to get elements in list

1. indexing - to extract single element

 a. forward/positive indexing
 ( first element - 0    last element - length-1) start from left to right'''

l=[10,20,30,40,50] 
print=(l[3])

'''b. backward/negative indexing (start fromright to left)'''
l=[10,20,30,40,50] 
print=(l[-1])

'''Nested list - list contain another list'''
l=[10,20,30,[100,200,300],40,50] 
print(l[4])
print(l[3][1])
print(l[-3])


l=[55,66,77[10,20,30,"jaykumar",["rahul",67],"john",45.67]]
print(l[3])
print(l[3][4])
print(l[3][4][0])

'''2. slicing- to extract multiple elements
[start:stop:step]
stop is not included'''
l=[10,20,30,40]
print(l[1:4])

l=[11,22,33,44,55,[100,200,300,500,600],"jay","ram",56]
print(l[5][1:4])
print(l[4:1:-1])

'''how to insert element in list
1. append() - add single element at the end
append()'''
l=[1,2,3,4]
l.append(100)
print(l)

'''extend() - add multiple elements at the end'''
l=[1,2,3,4]
l.extend([100,200,300])
print(l)

'''2. insert() - add element at particular index'''
l=[1,2,3,4]
l.insert(2,100)
print(l)

'''update() - var_name[index_no]=updated_value'''
l=[1,2,3,4]
l[2]=35
print(l)

'''reverse list'''
l=[1,2,3,4]
l.reverse()
print(l)

l=[18,2,53,40]
l.sort() #ascending order
print(l)

l.sort(reverse=True) #descending order
print(l)

#check if element exists in a list
l=[1,2,3,4]
print(5 in l)
print(4 in l)

list=[1,2,3,4]
for i in list:
    print (i)

'''
how to delete element

1.remove - 
2. pop - delete using index number -  var_name.pop(index)
3. del - del var_name[index]
4. clear - remove all elements from list
5. index - return index number of particular value'''