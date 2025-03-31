# display which is greater number than 20 by using append
numbers = [10, 25, 15, 30, 5, 40]  
greater_than_20 = []

for num in numbers:
    if num > 20:
        greater_than_20.append(num)

print("Numbers greater than 20:", greater_than_20)


# display even and odd numbers in given list
num=[23,10,56,79,45]
for n in num:
 if n%2==0:
    print("Number is even", n)
 else:
    print("Number is odd", n)

# display square of even numbers and cube of odd numbers
num = [23, 10, 56, 79, 45]
for n in num:
    if n % 2 == 0:
        print(f"Square of {n}: {n**2}")  # Using f-string
    else:
        print(f"Cube of {n}: {n**3}")  # Using f-string


# how do you check the element is present in list or not
num_list = [10, 20, 30, 40, 50]
element = 30

if element in num_list:
    print(f"{element} is present in the list.")
else:
    print(f"{element} is not present in the list.")

# Find the Sum of All Elements
num=[11,34,90,53,5]
sum=0
for i in num:
    sum=sum+i
print("Sum of all elements:" ,sum)

# Find the Largest Number.
num=[11,34,90,53,5]
print("Largest number is:",max(num))

# Remove Duplicates from a List


# Find Even Numbers in a List
num = [10, 15, 22, 33, 40, 55, 60]
even_numbers = [] 

for i in num:
    if i % 2 == 0:  
        even_numbers.append(i)

print("Even numbers:", even_numbers)


# Find Odd Numbers in a List
num = [10, 15, 22, 33, 40, 55, 60]
odd_numbers = []  

for i in num:
    if i % 2 != 0:  
        odd_numbers.append(i)

print("Odd numbers:", odd_numbers)


# Sort a List in Ascending Order.
num = [11,78,90,4,56]
print(num.sort())

# Merge Two Lists
n1 = [11, 78, 90, 4, 56]
n2 = [45, 33, 98, 2, 67]

n3 = n1 + n2  
print("Merged List:", n3)

# Find Common Elements in Two Lists


# Find the Second Largest Number
num = [11,78,90,4,56]
num.sort()
print("Second largest number is:", num[-2])

# Reverse a list in Python
num = [11,78,90,4,56]
print("reverse list:", num[::-1])

# Concatenate two lists index-wise


# Turn every item of a list into its square 
num = [2, 3, 4, 5, 6]
square_num = [] 

for i in num:
    square_num.append(i ** 2)

print("Squared list:", square_num)


# Concatenate two lists in the following order
l1 = [1, 56, 78, 9]
l2 = [54, 62, 1, 8]

l1.extend(l2)
print("Concatenated list:", l1)


# Iterate both lists simultaneously


# Remove empty strings from the list of strings 
l1 = ['', 1, 56, 73, '', 9]

while '' in l1: 
    l1.remove('')

print("Updated list:", l1)


# Add new item to list after a specified item


# Extend nested list by adding the sublist
l1 = [1, 2, [3, 4], 5]
sublist = [6, 7, 8]

l1[2].extend(sublist) 

print("Updated list:", l1)


# Replace list item with new value if found


# Remove all occurrences of a specific item from a list

