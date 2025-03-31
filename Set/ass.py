# Python Find missing and additional values in two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

missing_in_list1 = list(set2 - set1)  
additional_in_list1 = list(set1 - set2)  

missing_in_list2 = list(set1 - set2)  
additional_in_list2 = list(set2 - set1)  

print("Missing values in list1:", missing_in_list1)      
print("Additional values in list1:", additional_in_list1) 
print("Missing values in list2:", missing_in_list2)      
print("Additional values in list2:", additional_in_list2) 


# Python program to find the difference between two lists
s1 = [11, 22, 33, 44]
s2 = [33, 44, 55, 66]
s3 = set(s1)
s4 = set(s2)
s5 = s3.difference(s4)
print(list(s5)) 


# Python Set difference to find lost element from a duplicated array


# Python program to count number of vowels using sets in given string


# Concatenated string with uncommon characters in Python


# Python Program to accept the strings which contains all vowels


# Python Check if a given string is binary string or not


# Python set to check if string is panagram


# Python Set - Pairs of complete strings in two sets


# Python program to check whether a given string is Heterogram or not

