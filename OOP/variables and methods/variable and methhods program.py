class Employee:
    company_name="wipro" #static/class variables

    def __init__(self,name,designation,salary):
        self.name=name #instance variable
        self.designation=designation
        self.salary=salary

    #instance method
    def display(self): 
        print(f"name:{self.name} designation:{self.designation} salary:{self.salary}")

    #class method
    @classmethod
    def show(cls):
        print(f"company name:{cls.company_name}")

    @staticmethod
    def addnumber(num1,num2):
        ans=num1+num2
        print(f"add:{ans}")

    #local methods
    def total_salary(self):
        bonus=self.salary*10/100 #bonus, salary-- local variables-- not acesss to another functions
        total=self.salary+bonus
        print("total salary:",total)

emp1=Employee("john","HR",67000)
# emp1.display()

emp1.name="riya"
emp1.display()

emp1.total_salary() #local methods is access using ref variable

emp1.show() #classs method access by using object ref
Employee.show() #classs method access by using class name

emp1.addnumber(10,20) #static method access by using object ref
Employee.addnumber(10,20) #static method access by using class name

print(emp1.company_name) #static/class variables access by using ref variable
print(Employee.company_name) #static/class variables access by using class variable


emp2=Employee("blake","tester",47000)
emp2.display()