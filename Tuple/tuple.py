'''tuple                                      #list
1. non primitive datatype
2. comma sep values within ()                 #within []
3. () is not mandatory                        #[] is mandatory
4. immutable (not changable)                  #mutable
5. ordered(indexing, slicing)                 #ordered
6. heterogenous collection of elemnts         #
7. duplicate elements are allowed             #
8. (size)required less memory                 #required more memory
9. fast speed                                 #low speed
10. support packing and unpacking             #support only unpacking

syntax:
var_name=(va1,val2...)'''

t=(1,2,3,4)
print(t)
print(type(t))

n="riya","siya","ram"
print(type(n))  #() is not mandatory 

t1=(56)
print(type(t1)) 

#how to create tuple with single element
t2=(90,)
print(type(t2))

'''tuple                                      #set
1. non primitive datatype
2. comma sep values within ()                 #within {}
3. () is not mandatory                        #{} is mandatory
4. immutable (not changable)                  #mutable
5. ordered(indexing, slicing)                 #ordered
6. heterogenous collection of elemnts         #
7. duplicate elements are allowed 

'''

'''module- built in function'''

#how to check size of tuple
from sys import getsizeof
t=(1,2,3,4)
print(getsizeof(t)) #o/p - 72        #tuple- less memory than tuple and list (speed fast) 
print(id(t))

l=[1,2,3,4]
print(getsizeof(l)) #o/p - 88       #list - more memory than tuple but less memory than set(speed low than than tuple)
print(id(l))

s={1,2,3,4}
print(getsizeof(s)) #o/p - 216      #set - more memory than tuple and list (speed slow)
print(id(s))

'''unpacking - removing elements from tuple and stored it in a variable'''
t=(11,22,33) #tuple support unpacking
a,b,c=t
print(a)
print(b)
print(c)

l=[1,2,3] #list support unpacking
a,b,c=l
print(a)
print(b)
print(c) 

l={1,2,3} # set support unpacking
a,b,c=l
print(a)
print(b)
print(c)  

'''packing-  adding elements from variable to a tuple'''
x=111
y=222
z=333
t1=x,y,z
print(t1) #tuple allow packing

t3=(4,6,8,2,44,33,2,44,66,88,2,11,9)
print("lenght of tuple", len(t3))
print("min value", min(t3))
print("max value", max(t3))
print(t3.count(2))
print(sorted(t3)) #display in ascending order

'''how to add and element in tuple
1. to convert tuple into list
2. list--- add and delete #list(tup).append()
3. list covert to tuple'''

