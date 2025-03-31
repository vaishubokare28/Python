'''set logical program'''

# add list of elements to a set
list1=[1,2,3,4,5]
s=set(list1) # set constructor
print(s)

#return new set of identical items from two sets
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.intersection(s2)
print(s3)

#Get only unique items from two sets
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.symmetric_difference(s2)
print(s3)

#update the first set with items that don't exist in second set
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.difference_update(s2)
print(s3)

#remove items from the set at once
s1={11,22,33,44}
s2=s1.pop()
print(s2)
print(s1)

#return set of elements present in set A or B but not both
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.symmetric_difference(s2)
print(s3)

#check if two sets have any elemnets in common. if yes, display the common elements
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.intersection(s2)
print(s3)

#update set1 by adding items from set2, except common items
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.symmetric_difference_update(s2)
print(s3)

#remove items from set1 that are not common to both set1 and set2
s1={11,22,33,44}
s2={33,44,55,66}
s3=s1.difference_update(s2)
print(s3)