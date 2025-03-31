#write python program to find sum of squares of even numbers from list of integer using functional programming concept

from functools import reduce
l=[1,2,3,4,5,6,7,8,9,10]

even=list(filter(lambda n:n%2==0,l))
# print(even)

sq=list(map(lambda n:n**2,even))
# print(sq)

sum=reduce(lambda x,y : x+y,sq)
print("The sum of squares of even numbers: ",sum)



#given list of integers , write python program to calculate the product of all the elements in the list using functional programming concept
num=[1,2,3,4,5]
from functools import reduce
mul=reduce(lambda x,y:x*y,num)
print("The product of all the elments:",mul)



# #given list of string , write python program to filter string with length greater than 5 using functional programming concept
l=["apple","banana","cherry","dates","elderberry"]
greater=list(filter(lambda s:len(s)>5,l))
print(greater)


#write python program to filter odd number from list of interger using functional programming concept
num1=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda n:n%2!=0,num1))
print("List containing only even number:",odd)


#given a list of string, write python program to convert each string to uppercase using functional programming concept
l1=["apple","banana","cherrry"]
uppr=list(map(lambda n:n.upper(),l1))
print("List containing uppercase versions of string:",uppr)


#you are given list of numbers, write python programing calculating square of each number in the list using functional programming concept
num2=[1,2,3,4,5,6,7,8,9,10]
squ=reduce(lambda x,y:x+y,num2)
print("calculating square of each number in the list:",squ)


#palindrome string using using functional programming concept
str1=["121","madam","anuja","anuja","pooja"]
p=list(filter(lambda n:n==n[::-1],str1))
print("palindrome are:",p )


#Armstrong numbers using functional programming concept
n = [341, 153, 370, 677]
armstrong_numbers = list(filter(lambda num: num == sum(int(digit)**len(str(num)) for digit in str(num)), n))
print("Armstrong numbers are:", armstrong_numbers)



#to display string which contains i character
name=["prachi","anuja","priya","nisha","rahul","amruta"]
j=list(filter(lambda n:'i' in n,name))
print("Name containing i character:",j)


#to display string which starts from vowels
name1=["prachi","anuja","priya","nisha","esha","amruta"]
word = list(filter(lambda n: n[0].lower() in ('a', 'e', 'i', 'o', 'u'), name1))
print("Name satrting with vowels:",word)

#map and filter combined: extract uppercase and reverse them
#given a list of string, use map() to convert each string to uppercase and then use filter() to keep only the strings that have at least 3 character. finally reverse the list
str2 = ["apple", "banana", "cherry", "kiwi", "date"]
uppercased = list(map(lambda n: n.upper(), str2))
at_least_3 = list(filter(lambda n: len(n) >= 3, uppercased))
result = at_least_3[::-1]
print("Final list:",result)  


#reduce with initial value: fing GCD of list of numbers
#given list of numbers, use reduce() to calculate  greater common divisor(GCD) of all numbers
from functools import reduce
import math
num3 = [234, 678, 456, 123]
gcd = reduce(math.gcd, num3)
print("GCD  of the list:" ,gcd)  
