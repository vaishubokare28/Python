'''Basic Set Programs'''

# Find the size of a Set in Python
s={67,22,90,1,38,72}
print(len(s))

# Iterate over a set in Python
s={67,22,90,1,38,72}
for i in s:
    print(i)

# Python Maximum and Minimum in a Set
s={67,22,90,1,38,72}
print(max(s))
print(min(s))

# Python Remove items from Set
s={67,22,90,1,38,72}
s.remove(90)
print(s)

# Python - Check if two lists have at least one element common
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 5]

if set(list1) & set(list2):
    print("Lists have at least one common element.")
else:
    print("Lists have no common elements.")


# Python program to find common elements in three lists using sets
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

common_elements = set(list1) & set(list2) & set(list3)
print("Common elements:", list(common_elements))


# Python - Find missing and additional values in two lists
list1 = [1, 2, 3, 4, 5, 6, 10]
list2 = [4, 5, 6, 7, 8, 9, 10]

missing_values = list(set(list1) - set(list2))

additional_values = list(set(list2) - set(list1))

print("Missing values from list2:", missing_values)
print("Additional values in list2:", additional_values)

# Python program to find the difference between two lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

difference = list(set(list1) - set(list2))  
print("Difference:", difference)

# Python Set difference to find lost element from a duplicated array


# Python program to count number of vowels using sets in given string



# Advance Set Programs
# Python program to find union of n arrays

# Python - Intersection of two lists
s1={67,22,90,1,38,72}
s2={67,32,90,11,49,52}
s3=s1.intersection(s2)
print(s3)

# Python program to get all subsets of given size of a set


# Python - Minimum number of subsets with distinct elements using Counter


# Python dictionary, set and counter to check if frequencies can become same

