# 1. Create a text file named students.txt containing the following information:

#Name, Age, Grade
#John, 18, A
#Enma, 17, B
#Alex, 19, A
#Mia, 18, C

fs=open("students.txt","w")
fs.write("""
Name, Age, Grade
John, 18, A
Enma, 17, B
Alex, 19, A
Mia, 18, C""")



#2. Write a Python program to perform the following tasks:

#Task 1: Open the file and display its content.
#Task 2: Count and print the total number of lines in the file.
#Task 3: Add the following new student to the file: Sophia, 18, 8
#Task 4: Read the updated file and display its content again.
#Task 5: Create a new file called top students.txt and copy all students with grade 'A' from students.txt into it.
#Task 6-Write a python program to get the file size of a plain file.


fs=open("students.txt","w")
fs.write("""
Name, Age, Grade
John, 18, A
Enma, 17, B
Alex, 19, A
Mia, 18, C""")
