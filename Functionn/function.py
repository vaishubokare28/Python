#11 March 2025
''' functions
python supports
 1) statements
 2)functional programming
 3)oops statements'''


'''functions -it is collection of statements/set of instrucitons is called as function


types of fucntions
 
1)built-in functions-
print(),type(),id(),len(),append(),extend(),add(),update()
lower(), upper(), pop(),remove(),discard()

2)user defined functions- ap per user  requirements user create a function is called as user defined functions'''


'''how to create a  user defined fucntion:

syntax-

def function_name():
    statements


calling of funcitons-
function_name()'''

#for example-

def hello():
    print("welcome students")
hello()#calling fuction    

def school():
    print("this is my school")
#we can call one fucniton number of times
hello()
school()


def engineer():
    print("I am engineering student")
engineer()

'''
Advantage of function-
1)we can call fucntion anywhere in program and 
2)we can call one fucniton number of times
3)code Sreusability
4)large program is divide into fucnitons is called as modularity
5)easy to understand
6)reduce comlexity of function
7)easy maintain
8)easy testing and debugging
9)encapsulaiton/abstraction
10)memory optimization
11)avoid repetations
12)readability- we can easily read
13)increase efficiency


Disadvantages of fucntions
1)overhead in memory-
2)dependency issues
3)increased complexity for simple task

'''

#create a funcitons for addtion for 2 numbers
'''eval function- it will automatiocally determine the type of data'''

def add():
    a=20
    b=10
    c=a+b
    
    print("additon",c)
    
add()  #calling of fucnitons


def sub():
    a=20
    b=10
    d=a-b
    print("substration",d)
sub()    
    

#create a function calculate area of rectangle and area of circle

def rectangle():
    base=eval(input("enter the base value: ")) 
    height=eval(input("enter the height :"))

    area=(base*height)
    print("area of rectangle is:\n ",area)
rectangle()       

print()


def circle():
    radius=eval(input("enter the radius of circle: "))
    pi=3.14

    area_of_circle=2*pi*(radius**2)
    print("area of circle is: ", area_of_circle)
circle()    

print()


def greater_num():
    n1=eval(input("enter num1: "))
    n2=eval(input("enter num2: "))
    n3=eval(input("enter num3: "))

    if n1>n2 and n1>n3:
        print("greater number is: ",n1)

    elif n2>n3 and n2>n1:
        print("greater number is: ",n2)
    else:
        print("greater number is: ",n3)
greater_num()            


while True:
    print('''
       1.add
          2.substraction
          3.area of rectangle
          4.area of circle
          5.greater number
          6.exit
''')
    c=eval(input("Enter your choice= "))
    if c==1:
        add()
    elif c==2:
        sub()
    elif c==3:
        rectangle()
    elif c==4:
        circle()
    elif c==5:
        greater_num()    
    else:
        break


'''categories of function
1)without return type without parameter
2)wihtout return type with parameter
e.g'''
def add1(a,b):#=> this are the formal parameters
    c=a+b
    print("addition is: ",c)
add1(12,7)#=>this are the actual parameters    

'''
Mock topics-
dictionary
set
list
tuple
string
basic python
loops
Simple project-
'''


'''
interview questions
1)what is fucntions
2)explain advantages and disadvantages of functions
3)explain types of fucntions
4)how to create user defined function with example

'''