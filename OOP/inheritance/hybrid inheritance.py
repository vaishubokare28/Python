class student():
     def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

class subject(student):
    def __init__(self, rollno, name, part1 , part2):
         super().__init__(rollno, name)
         self.part1 = part1
         self.part2 = part2

class sports:
    def __init__(self, score):
        self.score = score

class result(subject,sports):
    def __init__(self, rollno, name, part1, part2, score):
        subject.__init__(self, rollno, name, part1, part2) 
        sports.__init__(self, score) 
        self.total = self.part1 + self.part2 + self.score
    def display(self):
         print(f"Roll No: {self.rollno}, Name: {self.name} "
                    f"Marks - Part1: {self.part1}/100, Part2: {self.part2}/100\n"
                    f"Sports Score: {self.score}/50\n"
                    f"Total Score: {self.total}/250")
r = result(10,"Yash",50,65,35)
r.display()