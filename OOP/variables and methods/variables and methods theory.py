'''variables- it is used to stored data

3 types-
1)local variables-

2)instance variables-
variables that belong to instance(object) of class
specific to each instance of class
defined within methods using self
separate copy is created for all objects
object variable is not shared between object
change made to instance variable by one object will not be reflected in other object

3)class/ static variables-
declared inside class and outside of the method
variables that are shared among all instance of class
common to all instance of class
when any value is common for all the objects then we create static variable to store this value
we can access using ref(object) variable and class name outside of class



methods -
3 types-
1)instance method - 
can acess instance variables inside a class
instance method is access by using object reference from outside class

2)class method -
within the method if we access class/static variables 
first argument of method is cls then it is called aas class method
it is mandatory to use @classmethod
we can acess class method by using object ref and class name but recommended to use class name only

syntax-
@classmethod
def method_name(cls):
 body(access static variables)

3)static method -
within the method if we access local variable then this method is called static method
it is mandatory to use @staticmethod
we can access static method by using ref and class name but reecommended to use class name only

syntax-
@staticmethod
def method_name(parameter):
 body(access local variables)

'''