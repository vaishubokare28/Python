# from abc import ABC, abstractmethod
# class Sample(ABC):
#     def show(self):
#         print("it is a non abstract method")
    
#     @abstractmethod
#     def get(self):
#         pass

# s=Sample()
# s.show()
# #TypeError: Can't instantiate abstract class Sample without an implementation for abstract method 'get'


# from abc import ABC, abstractmethod
# class RBI(ABC):

#     @abstractmethod
#     def IFSC_code(self):
#         pass

#     @abstractmethod
#     def home_loan(self):
#         pass

#     @abstractmethod
#     def gold_loan(self):
#         pass

# class SBI(RBI):
#     def IFSC_code(self):
#         print("IFSC code of SBI- SBI123")

#     def home_loan(self):
#         print("It provides 10% of home loan")

#     def gold_loan(self):
#         print("It provides 9% of gold loan")


# class ICIC(RBI):
#     def IFSC_code(self):
#         print("IFSC code of SBI- ICIC123")

#     def home_loan(self):
#         print("It provides 9% of home loan")

#     def gold_loan(self):
#         print("It provides 8% of gold loan")

# class HDFC(RBI):
#     def IFSC_code(self):
#         print("IFSC code of HDFC- HDFC123")

#     def home_loan(self):
#         print("It provides 8% of home loan")

#     def gold_loan(self):
#         print("It provides 7% of gold loan")

# s=SBI()
# s.IFSC_code()
# s.home_loan()
# s.gold_loan()

# i=ICIC()
# i.IFSC_code()
# i.home_loan()
# i.gold_loan()

# h=HDFC()
# h.IFSC_code()
# h.home_loan()
# h.gold_loan()

#create abstract base class- to claculate area of rectangle and area of circle
from abc import ABC, abstractmethod
class Calculate(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Calculate):
    def area(self,length,width):
        total1=length*width
        print(f"Area of rectangle:{total1}")

class circle(Calculate):
    def area(self,radius):
        total2=(3.14*radius*radius)
        print(f"Area of cicle: {total2}")

r=Rectangle()
r.area(2,4)

c=circle()
c.area(5)