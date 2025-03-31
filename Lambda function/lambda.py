'''lambda functions

1. function without name is called as anonymous function
2. lambda keyword
3. single line code
4. easy implementation
5. used only for expression and not used for loop, if else statements
6. use in higher order function- map(),filter(),reduce()

# syntax:
# variable_name=lambda arguments:expression

 '''

#addition of two numbers
sum=lambda a=10,b=20 : a+b
print(sum())

# to perform arithmetic operations (+.-,*,/) using lambda function
cal=lambda x=50,y=30 : (x+y,x-y,x*y,x/y)
print(cal())

'''
  Lambda function                                        Normal function
1. single line code                                    multiple line code
2. without function(anonymous function)                function having proper name(def function)
3. lambda keyword                                      def keyword
4. complexity lower                                    higher
5. not reusable                                        reusable

'''


#to display square of given no.

def square():
    n=3
    sq=n**2
    print(sq)
square()

 #using lambda
square=lambda n=3: n**2
print(square())

sq=lambda n=eval(input("enter n:")): n**2
print(sq())


#to display cube of given no.
def cube():
    n=3
    cb=n**3
    print(cb)
cube()

 #using lambda
cube=lambda n=3: n**3
print(cube())

cube=lambda n=eval(input("enter n:")): n**3
print(cube())


#calculate area of circle
circle=lambda r=eval(input("Enter radius of circle:")): 3.14*r*r
print(circle())

#calculate simple interest
sim_interest=lambda p=10, n=30, r=25: p*n*r
print(sim_interest())

#name="amruta"---uppercase
name=lambda n="amruta": n.upper()
print("uppercase:",name())

#calculate lenght of string
l=lambda name="amruta":len(name)
print(l())

#return digits 2346
string = lambda s="admin2346": "".join(c for c in s if c.isdigit())
print(string())


'''

Advantages 
1. one line code
2. can use anonymous funcion

Disadvantages
1. can't use multiple statements
2. reduce readability
3. hard to debug
4. 

'''