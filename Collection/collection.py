from collections import Counter
my_list=[1,2,3,1,2,14,5]
counter=Counter(my_list)
print(counter) #Counter({1: 2, 2: 2, 3: 1, 14: 1, 5: 1})

#to remove duplicate elements- to display unique elements

# for i in counter:
#     if counter[i]>1:
#         counter[i]=1
# print(counter)
print(counter.keys())# dict_keys([1, 2, 3, 14, 5])
# [1,2,3,14,5]


# d={}
# d[1]=1
# d[2]=4
# d[3]
# print(d) #KeyError: 3

import collections
d=collections.defaultdict(int)
d[1]=1
d[2]=4
d[3]
print(d) #defaultdict(<class 'int'>, {1: 1, 2: 4, 3: 0})

class Student:
    def __init__(self,n,a):
        self.name=n
        self.age=a
s1=Student('rahul',24)
print(s1.name)#rahul
s1.name="kunal"
print(s1.name)#kunal

import collections
Student=collections.namedtuple('Student',['name','age'])
s1=Student('rahul',23)#object1
s2=Student('rajesh',25)#object2
print(s1.name)#rahul
print(s2.age)#25
print(s2.name)#rajesh
# s1.age=27  #   AttributeError: can't set attribute
# print(s1.age)