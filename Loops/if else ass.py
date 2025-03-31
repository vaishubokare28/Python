# 1234@thekiranacademy.com


#swapping of two numbers using third variable without using it
a = 5
b = 10
print("Before swapping: a =", a, "b =", b)

temp = a  
a = b     
b = temp  

print("After swapping: a =", a, "b =", b)


#swapping of two numbers without third variable
a=2
b=5

a=a+b
b=a-b
a=a-b

print(a)
print(b)


#Company decide to give bonus of 5% to employee. If his/her year of service is more than 5 years
years_of_service = int(input("Enter your years of service: "))

if years_of_service > 5:
    print("You are eligible for a bonus of:")
else:
    print("You are not eligible for a bonus.")


#student will not allowed to sit his/her attendance is less than 75%
classes_held = int(input("Enter the total number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100
print("Attendance Percentage:",attendance_percentage)

if attendance_percentage >= 75:
    print("Student is allowed to sit in the exam.")
else:
    print("Student is NOT allowed to sit in the exam.")


#check whether profit or loss
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    print("Profit:" , selling_price - cost_price)
else:
    print("Loss:",cost_price - selling_price)
