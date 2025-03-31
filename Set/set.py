'''
Set datatype (non primitive datatype)
1. comma sep values within {}
2. var_name={val1,val2,...}
3. unordered collection of datatype (indexing and slicing not allowed) 
4. duplication not allowed
5. heterogenous collection of immutable element
6. we can add, delete element but not update elements in set (mutable)

'''

s={10,20,30,40,50}
print(s)
print(type(s))

s1={10,20,(30,40,50)}
print(s1) #tuple is allowed in set

# s2={10,20,[30,40,50]}
# print(s2) #error - list is mutable


'''How to add element in set

add() - add new element in a set 
  var_name.add(value)'''

fruites={"mango","apple","banana"}
fruites.add("cherry")
print(fruites)


'''update() - merge to sets'''

color={"red","orange","yellow"}
fruites.update(color)
print(fruites)

'''How to delete element in set

remove()
varname.remove(value)'''

fruites={"mango","apple","banana","cherry","orange"}
fruites.remove("apple")
print(fruites)

#fruites={"mango","apple","banana","cherry","orange"}
# fruites.remove("grapes")
# print(fruites) #if element is not present in set then remove will throws error - keyerror

''' discard()'''

fruites={"mango","apple","banana","cherry","orange"}
fruites.discard("apple")
print(fruites)

fruites={"mango","apple","banana","cherry","orange"}
fruites.discard("grapes")
print(fruites) #if element is not present in set then discard will not throws error 

''' pop()'''
fruites={"mango","apple","banana","cherry","orange"}
delete=fruites.pop()
print(delete)
print(fruites)

#How to create set by using set constructor
s=set()
print(s)

s.add("john")
print(s) #only single element can be add using add()

n={"riya","priya","siya"}
s.update(n)
print(s) #to add multiple elements we can use update()

#to remove all elements in set using clear()
s={"riya","priya","siya"}
s.clear()
print(s) 

#to count no.of elements present in set 
fruites={"mango","apple","banana","cherry","orange"}
print(len(fruites))

fruites={"mango","apple","banana","cherry","orange"}
for i in fruites:
    print(i)


'''union()- joins to or multiple sets'''
s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.union(s2)
print(s3) #all elements are display and duplicates are not allowed

'''intersection()- display duplicate elements'''
s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.intersection(s2)
print(s3) #display duplicate elements

'''difference()- will return a new set that will contain only items from first set'''
s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.difference(s2)
print(s3)

'''symmetric_difference() - All elements are display except duplicate elements'''
s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.symmetric_difference(s2)
print(s3) #all elements are display except duplicate elements

'''issubset() '''
s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.issubset(s2)
print(s3) #all elements of set1 should be present in set2 - true

'''issuperset() - all elements in child will be present in parent then it will return true otherwise it returns false'''
s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.issuperset(s2)
print(s3) #all elements of set2(child element) should be present in set1(parent element) - true

s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.difference_update(s2)
print(s3)

s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.intersection_update(s2)
print(s3)

s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.isdisjoint(s2)
print(s3)

s1={11,22,33,44,55}
s2={44,55,66,77,88}
s3=s1.symmetric_difference_update(s2)
print(s3)

