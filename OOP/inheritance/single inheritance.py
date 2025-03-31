#single inheritance
'''syntax:

class Parent:
 pass
class Child(Parent):
 pass

c=Child()'''


class Parent:
    def property1(self):
        print("Farm and House")

class Child(Parent):
    def property2(self):
        print("BMW Car and Gold")
    
c=Child()
c.property1()
c.property2()


#super() - it inherits properties(variable), methods and constructor in child class from parent class
#method overriding (run time polymorphism)
class Parent: 
    def property(self):
        print("Farm and House")

class Child(Parent):
    def property(self):
        super().property()
        print("BMW Car and Gold")
    
c=Child()
c.property()


