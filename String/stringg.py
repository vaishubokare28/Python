#  String methdos-

# 1)len()-    to calculate length of a string
# emp_name="amit patil"
# print("length of the string = ",len(emp_name))

# 2)upper()-To convert string to uppercase
# syntax= varname.upper()
# course="python"
# print(course.upper())

# 3)lower()- to convert string to lower case
# syntax-  varname.lower()
# course="TESTING"
# print(course.lower())

# 4)title()- to captilize every word first letter
# name="the kiran academy"
# print(name.title()) #The Kiran Academy

# /name="the kiran academy"
# print(name.capitalize()) #The kiran academy

# 6)isalpha()-   string contains only alphabets it returns TRUE otherwise false
# student="john"
# print(student.isalpha())     #True

# student="john34567"
# print(student.isalpha()) # False

# 7)isdigit()/ isnumeric()
# price="70000"
# print(price.isdigit())#true

# price="70Lac"
# print(price.isdigit())#false

# 8)alnum-
# print(price.isalnum()) 








# 1)split()-
str1="python is a dynamic language"
res=str1.split()
print(res)  #['python','is','a','dynamic','language']

str2="python is a simple language"
s=str2.split(sep=" ")
print(s)

s1="the ki@ran a@cademy"
s2=s1.split(sep='@')
print(s2)
#['the ki','ran a','cademy']

#2)replace()-
st1="python is a dynamic language,python is a simple language"
r=st1.replace('python','javascript')
print(r)

# 3)count()-  count occurance of a character
name="amruta"
c=name.count("a")
print(c)

#1)To display length of a string
s1="amit patil"  #10-1= 9
count = 0
for i in s1:
   if i != " ":
       count = count + 1

print(f"The length of srtring with out space length is: {count}")

s1 = "amit patil" #10-1=9
r=len(s1.replace(" ",""))
print("length of the string= ",r)

#2)To count no of words in a given string
str2="python is a simple language"
# words=5
words = len(str2.split())
print("no of words= ",words)

#3)To count no of vowels and consonent in a given string
str="kiran academy"
vowels=0
consonent=0
l=len(str)
for i in range(l):
    if str[i].isalpha():
       if (str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
           vowels=vowels+1
       else:
            consonent=consonent+1

print("no of vowels= ",vowels)
print("no of consonent= ",consonent)

#4) Find all occurrences of a substring in a given string by ignoring the case
#Write a program to find all occurrences of “USA” in a given string ignoring the case.
str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "USA"

print(len(str1.split('usa')))














