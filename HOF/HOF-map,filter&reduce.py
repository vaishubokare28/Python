'''Higher order function - it is function which takes other function as arguments

1. map() 
2. filter()
3. reduce()
'''

'''map() - function is HOF which takes function and sequence as argument

syntax: variable_name= map(lambda arguments:expression,sequence/iterable)'''

l=[1,2,3,4,5]
sq=[]
for i in l:
    sq.append(i**2)
print(sq)

#to display square of every numbers using map() function
num=[1,2,3,4,5]
sq=list(map(lambda n:n**2,num))
print(sq)

#to display cube of every numbers using map() function
num=(1,2,3,4,5)
cube=tuple(map(lambda n:n**3,num))
print(cube)

#to increase marks by 5
marks=[50,60,70,80,90]
inc=list(map(lambda m:m+5,marks))
print(inc)

#convert into uppercase
emp_name=["john","martin","blake","tiger"]
upper=list(map(lambda s:s.upper(),emp_name))
print(upper)

#to increase salary by 10000
emp_name={"Om":51000,"sakshi":45000,"Priya":43000,"Rahul":4900}
print(emp_name.items())
in_sal=dict(map(lambda n:(n[0],n[1]+10000),emp_name.items()))
print(in_sal)

#to decrease marks by 5
stu_name={"Om":51,"sakshi":45,"Priya":43,"Rahul":49}
de_marks=dict(map(lambda n:(n[0],n[1]-5),stu_name.items()))
print(de_marks)


'''filter() - 
synatx: filter(lambda,itertor)
'''

l=[1,2,3,4,5,6,7,8,9,10]
even=[]
for i in l:
    if i%2==0:
        even.append(i)
print(even)

#to display even numbers using filter() function
l=[1,2,3,4,5,6,7,8,9,10]
even=list(filter(lambda n:n%2==0,l ))
print(even)

#to dispaly odd numbers using filter() function
l=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda n:n%2!=0,l))
print(odd)

#to display negative numbers using filter() function
num=[67,-56,88,-34,-12,-85]
neg=list(filter(lambda n:n<0,num))
print(neg)

#to display person who is eligible for voting
person={"anuj":34,"priya":17,"prachi":25,"nisha":15,"nikita":56}
print(person.items())
eligible=dict(filter(lambda n:n[1]>=18,person.items()))
print(eligible)
print(eligible.keys())

'''reduce()
syntax: reduce(lambda,iterable)
'''

num=[1,2,3,4,5]
sum=0
for i in num:
    sum=sum+i
print(sum)

#sum of all numbers using reduce() function
from functools import reduce
num=[1,2,3,4,5]
sum=reduce(lambda x,y : x+y,num)
print(sum)

#to display multiplication of all numbers using reduce() function
from functools import reduce
l=[1,2,3,4,5]
mul=reduce(lambda x,y: x*y,l)
print(mul)


'''real world example-
amazon shopping app
map() function used to search the products
filter() function is used to filter the products as per our requirements
reduce() function used to sum all the cost of products'''