
# l={1,2,3,4,5}
# d={}
# for num in l:
#    d[num]=num*num  
# print(d)


'''using dictionary comprehension-
syntax-
{Key:value for var in sequence}'''
l={1,2,3,4,5}
sq={num:num*num for num in l}
print(sq) 

# To increse marks by 5
result={'aniket':67,'sonu':56,'om':76,'abhi':35,'tejas':25}
inc={name:marks+5  for name,marks in result.items()}
print(inc) 

'''syntax-{key:value for var in sequence if condition}'''

#To display students whose marks is less than 60
less={name:marks for name,marks in result.items() if marks<60}
print(less) 

'''if else  syntax-
{exp1 if cond else exp2 for var in sequence}'''

# to display pass or fail status if students marks is greater than 40
result={'aniket':67,'omkar':56,'om':76,'abhi':35,'tejas':25}
status=['pass' if marks>40 else 'fail' for marks in result.values()]
print(status)


# Create a nested dictionary with student names as keys and their marks and pass/fail status as values
status_dict = {student: {'marks': marks, 'status': 'pass' if marks > 40 else 'fail'} 
               for student, marks in result.items()}

# Display the result
print(status_dict)


# Grades Logic:

# If marks are 70 or more, the grade is 'A'.
# If marks are 50 or more but less than 70, the grade is 'B'.
# If marks are 40 or more but less than 50, the grade is 'C'.
# If marks are less than 40, the grade is 'F' (indicating failure).

# Create a nested dictionary with student names as keys and their marks, pass/fail status, and grade as values
status_dict = {
    student: {
        'marks': marks,
        'status': 'pass' if marks > 40 else 'fail',
        'grade': 'A' if marks >= 70 else 'B' if marks >= 50 else 'C' if marks >= 40 else 'F'
    } 
    for student, marks in result.items()
}

# Display the result
print(status_dict)

#to display person who is eligible for voting
person={'aniket': 19, 'sonu':34, 'om': 15, 'abhi': 35, 'tejas': 17}
voting={name:age for name,age in person.items() if age>=18}
print(voting)

vot=['Eligible' if age>=18 else 'Not Eligible' for age in person.values()]
print(vot)


squares = {num: num**2 for num in range(1,11)}
print(squares)