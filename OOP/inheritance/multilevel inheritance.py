class Company:
    def __init__(self,comp_name,location):
        self.comp_name=comp_name
        self.location=location

class Manager(Company):
    def __init__(self,comp_name,location,m_name,dept):
      super().__init__(comp_name,location)
      self.m_name=m_name
      self.dept=dept

class Worker(Manager):
    def __init__(self,comp_name,location,m_name,dept,w_name,salary):
        super().__init__(comp_name,location,m_name,dept)  
        self.w_name=w_name
        self.salary=salary

    def display(self):
        print(f"comapany name:{self.comp_name} Location:{self.location} Manager name:{self.m_name} department:{self.dept} worker name:{self.w_name} slaray:{self.salary}")

s=Worker("wipro","pune","John deo","Admin","aniket",56000)
s.display()
