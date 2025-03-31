#Set Comprehension

# 1. Find Common Elements
# Given two lists listi and list2, write a set comprehension that creates a set of the common elements between these two lists.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common_elements = {x for x in list1 if x in list2}
print("Common Elements:", common_elements)

# 2. Remove Duplicates
# You are given a list of integers, write a set comprehension to remove any duplicate values from the list.
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_numbers = {x for x in numbers}
print("Unique Numbers:", unique_numbers)

# 3. Multiples of 3 and 5
# Write a set comprehension to generate a set of numbers that are multiples of either 3 or 5 from 1 to 50 (inclusive).
multiples = {x for x in range(1, 51) if x % 3 == 0 or x % 5 == 0}
print("Multiples of 3 or 5:", multiples)

