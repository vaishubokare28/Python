# List comprehension

# 1. Nested List Comprehension
# Write a list comprehension that flattens a 20 list (a list of lists) into a 1D list. For example, from [[1, 2], [3, 4], [5, 6]] create the list [1, 2, 3, 4, 5, 6]

# 2. Find Prime Numbers
# Write a list comprehension to generate a list of all prime numbers between 1 and 50.

# 3. Create a List of Tuples
# Given a list of numbers, write a list comprehension to create a list of tuples where each tuple contains the number and its square.
numbers = [1, 2, 3, 4, 5]

tuples = [(num, num ** 2) for num in numbers]
print("List of Tuples:", tuples)

# 4. Reverse Strings in a List
# Given a list of strings, write a list comprehension to create a new list where each string is reversed.
strings = ["hello", "world", "python", "code"]

reversed_strings = [s[::-1] for s in strings]
print("Reversed Strings:", reversed_strings)

# 5. Sum of Digits
# Given a list of integers, write a list comprehension to create a list where each element is the sum of the digits of the corresponding integer.

# 6. Find Common Elements in Two Lists
# Write a list comprehension to find the common elements between two lists and return them in a new list.
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

common = [x for x in list1 if x in list2]
print("Common Elements:", common)

# 7. Flatten a List of Lists with Conditions.
# Given a list of lists, write a list comprehension that flattens the list and only includes numbers greater than 5.