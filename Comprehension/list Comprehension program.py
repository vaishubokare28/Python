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



fruits = ['mango', 'kiwi', 'strawberry', 'cherry', 'grapes', 'orange', 'apple']

# Exercise 1 - rewrite the above example code using list comprehension syntax.
 # a variable named uppercased_fruits to hold the output of the list comprehension.
 # Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce 
# output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(capitalized_fruits)

# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. 
# Hint: You'll need a way to check if something is a vowel.

# Exercise 4 - make a variable named fruits_with_only_two_vowels. 
# The result should be ['mango', 'kiwi', 'strawberry']
# fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowel(fruit) == 2]
# print(fruits_with_only_two_vowels)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
fruits_with_more_than_five_chars = [fruit for fruit in fruits if len(fruit) > 5]
print(fruits_with_more_than_five_chars)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
fruits_with_exactly_five_chars = [fruit for fruit in fruits if len(fruit) == 5]
print(fruits_with_exactly_five_chars)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
fruits_with_less_than_five_chars = [fruit for fruit in fruits if len(fruit) < 5]
print(fruits_with_less_than_five_chars)

# Exercise 8 - Make a list containing the number of characters in each fruit. 
# Output would be [5, 4, 10, etc... ]
fruit_name_lengths = [len(fruit) for fruit in fruits]
print(fruit_name_lengths)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if 'a' in fruit]
print(fruits_with_letter_a )

numbers=[34,26,89,56,45,78,11]
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)

number1=[13,-67,45,-89,-34,55]
# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [num for num in number1 if num > 0]
print(positive_numbers)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [num for num in number1 if num < 0]
print(negative_numbers)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
number3=[23,567,4,8900,45,32,1]
numbers_with_two_or_more_digits = [num for num in number3 if abs(num)>= 10]
print(numbers_with_two_or_more_digits)

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. 
# Output is [4, 9, 16, etc...]
number2=[2,3,4,5]
numbers_squared = [num ** 2 for num in number2]
print(numbers_squared)

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [num for num in number1 if num < 0 and num % 2 != 0]
print(odd_negative_numbers)

# Exercise 17 - Make a variable named numbers_plus_5. 
# In it, return a list containing each number plus five.
numbers_plus_5 = [num + 5 for num in numbers]
print(numbers_plus_5)
