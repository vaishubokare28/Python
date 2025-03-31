''' Polymorphism - many forms

Types:
1. comple time polymorphism 
2. run time polymorphism 

1) comple time polymorphism 
a. method overloading
b. operator overloading
##Python does not support method overloading and operator overloading

2) run time polymorphism 
a. method overrinding 
'''


# class Calculator:
#     def sum(self,a,b):
#         self.total=self.a+self.b
#         print(self.total)
#     def sum(self,a,b,c):
#         self.total=self.a+self.b+self.c
#         print(self.total)

# cal=Calculator()
# cal.sum(10,20)  #Python does not support method overloading and operator overloading because python is dynamically language
# cal.sum(10,20,30)
    

#using (*args, **kwargs) we can use method overloading python
#1. *args
#* used whrn we don't know how many arguments will passed into our function
def sum(*args):
    sum=0
    for i in args:
        sum=sum+i
    print(f"sum: {sum}")


sum(2,3)
sum(4,6,8)
sum(3,5,7,9)

#arbitary argument
#if you don't know how many arguments that will be passed into our function
#add * before parameter name in function defination

def person(*args):
   print("youngest:",args[4])
   print("oldest:",args[0])

person("ashwin","shyam","priya","riya","ram")


#2. **kwargs keyword argument
#**used when we have keywords argument
def function(**kwargs):
   print(kwargs['lname'])

function(fname="john",lname="deo")