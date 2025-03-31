class TKA:
    def __init__(self,batch_no,course):
        self.batch_no=batch_no
        self.course=course

class Student(TKA):
    def __init__(self,batch_no,course,roll_no,name,marks):
        super().__init__(batch_no,course)
        self.roll_no=roll_no
        self.name=name
        self.marks=marks

    def display(self):
        print(f"batch no: {self.batch_no} course:{self.course} roll no:{self.roll_no} name:{self.name} marks:{self.marks}")

obj1=Student(1048,"python",1,"riya",78)
obj1.display()
        