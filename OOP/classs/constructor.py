# class Student:
#     def __init__(self, rollno, name, marks):   
#         self.rollno = rollno   
#         self.name = name       
#         self.marks = marks    

#     def show(self):
#         print(f"Rollno:{self.rollno}, Name:{self.name}, Marks:{self.marks}")

# obj1 = Student(1, "amruta", 78)
# obj1.show()
# obj2 = Student(2, "nisha", 80)
# obj2.show()
# obj3 = Student(3, "aniket", 89)
# obj3.show()


'''__init__
It is automatically executed when object of class is created
This method is useful to initialize the variables of class object


self
It is reference variable which is pointing to current object
use of self is to access the functionality of object within class
'''


class Product:
    def __init__(self, id, name, quantity, price):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def show(self):  
        print(f"ID:{self.id}, Name:{self.name}, Quantity:{self.quantity}, Price:{self.price}")

    def sum(self):
        self.total=self.quantity*self.price
        print(f"Total:{self.total}")

obj1 = Product(101, "pen", 50, 25)
obj1.show()
obj1.sum()
obj2 = Product(102, "Book", 12, 250)
obj2.show()
obj2.sum()





