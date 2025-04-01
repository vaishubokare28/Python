# Exercise 1: Create a dictionary with numbers and their squares
# Create a dictionary where the keys are integers from 1 to 10, and the values are the square of those integers.

squares = {num: num**2 for num in range(1,11)}
print(squares)

# Exercise 2: Filter even numbers
# Given a list of integers, create a dictionary where the keys are the even numbers from the list, and the values are those numbers multiplied by 2.

l=[1,2,3,4,5,6,7,8,9,10]
mul={num:num**2 for num in l if num%2==0}
print(mul)

# Exercise 3: Create a dictionary with word lengths
# Given a list of words, create a dictionary where the keys are the words, and the values are the lengths of those words.

words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)


# Exercise 4: Swap keys and values
# Given a dictionary where the keys are names of people and the values are their ages, create a new dictionary where the ages are the keys and the names are the values.
ages = {"Alice": 25, "Bob": 30, "Charlie": 35}
swapped = {age: name for name, age in ages.items()}
print(swapped)

# Exercise 5: Remove items with a value less than 50
# Given a dictionary with student names as keys and their scores as values, create a new dictionary that only contains students with scores greater than or equal to 50.
scores = {"Alice": 45, "Bob": 75, "Charlie": 30, "David": 60}
filtered_scores = {name: score for name, score in scores.items() if score >= 50}
print(filtered_scores)

# Exercise 6: Create a dictionary with frequency count
# Given a list of integers, create a dictionary that counts the frequency of each number in the list.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
frequency = {num: numbers.count(num) for num in set(numbers)}
print(frequency)

# Exercise 7: Create a dictionary from two lists
# Given two lists: one with student names and the other with their corresponding scores, create a dictionary where the student names are the keys and the scores are the values.
students = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
student_scores = {students[i]: marks[i] for i in range(len(students))}
print(student_scores)

# Exercise 8: Generate a nested dictionary with grades
# Given a list of students and their corresponding marks, create a nested dictionary where each student is a key, and their value is a dictionary containing their marks and a "pass/fail" status. The "pass" status should be given to students who scored above 40.
students = ["Alice", "Bob", "Charlie"]
marks = [85, 30, 78]
grades = {students[i]: {"marks": marks[i], "status": "pass" if marks[i] > 40 else "fail"} for i in range(len(students))}
print(grades)

# Exercise 9: Filter out vowels from a string
# Given a string, create a dictionary where the keys are the characters from the string (excluding vowels), and the values are the number of times each character appears in the string.
string = "hello world"
vowels = "aeiou"
char_count = {char: string.count(char) for char in string if char not in vowels and char != " "}
print(char_count)

# Exercise 10: Create a dictionary with cubes of odd numbers
# Given a range of numbers from 1 to 20, create a dictionary where the keys are the odd numbers, and the values are the cubes of those odd numbers.
cubes = {num: num**3 for num in range(1, 21) if num % 2 != 0}
print("Exercise 10:", cubes)