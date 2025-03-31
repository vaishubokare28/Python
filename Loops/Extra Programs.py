# '''Control Flow'''
# #1.To display number is positive or negative
# n=int(input("enter a number:"))
# if n>=0:
#     print(f"{n} is positive number")
# else:
#     print(f"{n} is negative number")

# #2.To display person who is eligible for voting 
# age=int(input("Enter your age:"))
# if age>=18:
#     print("your are eligible for voting")
# else:
#     print("Not eligiblr for voting")

# #3.Write a python program to display number is even or odd
# num=int(input("Enter a number:"))
# if num%2==0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")

# #4.Write a python program to check year is leap or not
# yr=int(input("Enter a year:"))
# if yr%4==0:
#     print(f"{yr} is a leap year")
# else:
#     print(f"{yr} is not a leap year")

# #5.Write a python program to  check number is divisible by 3 or 5.
# number=int(input("Enter a number:"))
# if number%3==0 or number%5==0:
#     print(f"{number} is divisible by 3 or 5")
# else:
#     print(f"{number} is not divisible by 3 or 5")



# '''If Else'''
# #1.To check character is vowels or not
# ch=input("Enter a character:")
# if ch=='a' or 'e' or 'i' or 'o' or 'u':
#     print(f"{ch} is vowel")
# else:
#     print(f"{ch} is not a vowel")


# # 2.A company decided to give bonus of 5 % to employee .if his/her year of service is more than 5 years.
# # ask user for their salary and year of service and print the net bonus amount.
# salary=float(input("Enter salary:"))
# year=int(input("Enter year of service:"))
# if year>5:
#     bonus=salary*5/100
#     print(f"Bonus amount:{bonus}")
# else:
#     print("No bonus")

# #3.A student will not allowed to sit  in exam if his/her attendance is less than 75%.
# # Take the input from user 
# # Number of classes held.
# # number of classes attended
# # and print 
# # percentage of class attended 
# # is student is allowed to sit in exam or not.
# classes_held=int(input("Enter number of classes held:"))
# classes_attended=int(input("Enter number of classes attended:"))
# attendance_percentage=(classes_attended/classes_held)*100
# if attendance_percentage<75:
#     print(f"{attendance_percentage:.2f}% is less than 75%. Student will not allowed to sit in exam")
# else:
#     print("Student will allowed to sit in exam")

# # 4.Write a python program to find the eligibility of admission for a professional course based on the 
# # following criteria: Go to the editor
# # Marks in Maths >=65
# # Marks in Phy >=55
# # Marks in Chem>=50
# # Total in all three subject >=180
# maths=int(input("Enter marks in maths:"))
# physics=int(input("Enter marks in physics:"))
# chemistry=int(input("Enter marks in chemistry:"))

# total=maths+physics+chemistry
# if maths >= 65 and physics >= 55 and chemistry >= 50 and total >= 180:
#     print("Eligible for admission")
# else:
#     print("Not eligible for admission")

# # #5.write a python program to calculate profit and loss .

# # sp =  1000   600
# # cp=   800    900

# # profit=  200
# sp=int(input("Enter selling price:"))
# cp=int(input("Enter cost price:"))
# if sp>cp:
#     profit=sp-cp
#     print("Profit:",profit)
# else:
#     loss=cp-sp
#     print("loss:",loss)


# '''Else If Ladder'''
# # 1)Write a python program to check triangle is valid or not .
# side1=int(input("Enter side1:"))
# side2=int(input("Enter side2:"))
# side3=int(input("Enter side3:"))
# total_side=side1+side2+side3
# if total_side==180:
#     print("Triangle is valid")
# else:
#     print("Triangle is not valid")

# # 2)Write a python program to check character is alphabeats,digits or special symbols.
# # Get input from the user
# char = input("Enter a character: ")

# # Check if it is an alphabet, digit, or special symbol
# if char.isalpha():
#     print(f"{char} is an alphabet.")
# elif char.isdigit():
#     print(f"{char} is a digit.")
# else:
#     print(f"{char} is a special symbol.")


# # 3)Program To Check whether a Triangle is Equilateral, Isosceles or Scalene .
# # Get the sides of the triangle
# side1 = float(input("Enter side 1: "))
# side2 = float(input("Enter side 2: "))
# side3 = float(input("Enter side 3: "))

# # Check the type of triangle
# if side1 == side2 == side3:
#     print("The triangle is Equilateral.")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is Isosceles.")
# else:
#     print("The triangle is Scalene.")


# # 4)write  a python program to check  entered date is valid or not.


# # 5)write  a python program to display largest no among two numbers.
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# if num1 > num2:
#     print(f"The largest number is: {num1}")
# elif num2 > num1:
#     print(f"The largest number is: {num2}")
# else:
#     print("Both numbers are equal.")


# #1.To accept 3 numbers and display greater number  among it.
# a= int(input("Enter a= ")) 
# b= int(input("Enter b= "))  
# c= int(input("Enter c= "))  

# if a>b and a>c:   
#     print("a is a greater")

# elif b>a and b>c:
#      print("b is a greater")
      
# elif c>a and c>b:
#      print("c is a greater")
# else:
#      print("please enter valid no")

# # 2)Accept any  city from the user and display monument of that city.
# # city             monument
# # Delhi            Red Fort
# # Agra             Taj Mahal
# # Jaipur           Jai Mahal

# city = input("Enter name of city:")
# if city == "Delhi":
#     print("monumemt of delhi is red fort")
# elif city == "Agra":
#     print("monument of agra is taj mahal")
# elif city=="jaipur":
#     print("monument of jaipur is jai mahal")
# else:
#     print("Please enetr valid city name")

# 3)write a python program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
# cost price(in rs)                         Tax
# >100000                                    15%
# >50000 and <=100000                        10%
# <=50000                                     5%

# price= int(input("Enter cost price of a bike= "))

# if price>100000:
#       tax= price * 15/100
# elif price>50000 and price<=100000:
#       tax=price * 10/100
# elif price<=50000:
#        4000
# else:
#       print("please enter valid price")

# print("bike price= ",price," tax= ",tax)

# #4).Accept a number from 1 to 7 and display the name of the day like 1 for sunday ,2 for monday and so on.
# num = int(input("Enter a number 1-7: "))
# if num == 1:
#      print("Sunday")
# elif num == 2:
#      print("Monday")
# elif num == 3:
#      print("Tuesday")
# elif num == 4:
#      print("Wednesday")
# elif num == 5:
#      print("Thursday")
# elif num == 6:
#      print("Friday")
# elif num == 7:
#      print("Saturday")
# else:
#     print("Please enter a number between 1 and 7.")

# #1) Enter basic salary >=10000 from user then calculate 
# # hra  will be 10% of bs, ta will be 5%  of bs ,bonus=2400
# # otherwise  hra=5% of bs,ta=1200,bonus=1000
# # then calculate netsal of the employee
# # netsal=bs+hra+ta+bouns

# bs=int(input("Enter bs="))
# if bs>=10000:
#     hra=bs*10/100
#     ta=bs*5/100
#     bonus=2400
# else:
#     hra=bs*5/100
#     ta=1200
#     bonus=1000
# netsal=bs+hra+ta+bonus
# print("hra= ",hra)
# print("ta= ",ta)
# print("bonus=",bonus)
# print("netsal= ",netsal)

# 1)Enter 5 subjects marks and calculate its sum and percentage

# percentage >=75    ---- Distinction
# percentage >=60-----    First class
# percentage >=50----     Second class
# percentage >=40  ---- pass
    
# otherwise Fail

# s1=int(input("Enter s1= "))  
# s2=int(input("Enter s2= "))  
# s3=int(input("Enter s3= "))  
# s4=int(input("Enter s4= "))  
# s5=int(input("Enter s5= "))  

# sum=s1+s2+s3+s4+s5
# print("sum= ",sum)
# per=(sum/500)*100
# print("percentage= ",per)

# if per>=75:
#     print("Distinction")
# elif per>=60:
#     print("First class")
# elif per>=50:
#     print("Second class")
# elif per>=40:
#     print("pass")
# else:
#     print("fail")


# 3)Write a python program to calculate electricity bill (accept number of units from users according to the following criteria:

# unit                         Price
# First 100 units               no charge
# Next 100 units                Rs.5 per unit
# After 200 units               Rs.10 per unit

# for eg- if input unit is 350 then total bill amount is-rs2000)

# unit = int(input("Enter Unit"))

# if unit <= 100:
#     bill = 0
#     print("Bill 0")
# elif unit<=200:
#     bill =(unit-100) *5   
#     print("Bill is ", bill)
# else:
#     bill = ((unit-200)*10 + (100*5))
#     print("Bill is ", bill)


# units = int(input("Enter Units : "))
# if (units <=100):
#      print("No charges on units")
# elif (units>100)and(units<=200):
#     charges = (units-100) *5
#     print("charges= ",charges)
# elif(units>200):
#     charges = (units-200)*10 + (100)*5
#     print("charges=",charges)



# 1.to display 1 to 1o numbers
# for i in range(1,11):
#     print(i)

# 2.to display even numbers from 1 to 20
# 2 4 6 8 10 12 14 16 18 20
# for i in range(2,21,2):
#     print(i)

# #3.to display odd numbers from 1 to 100
# for i in range(1,100,2):
#     print(i)


# #To display even numbers from 1 to 100
# for i in range(1,100):
#    if i%2==0:
#        print(i)

# #To display odd numbers from 1 to 100
# for i in range(1,100):
#    if i%2!=0:
#        print(i)

# To display 10 to 1 numbers
# op-10 9 8 7 6 5 4 3 2 1
# for i in range(10,0,-1):
#     print(i)

# to display odd numbers from 32 to 21
# for i in range(31,20,-2):
#      print(i)

# for i in range(32,20,-1):
#      if i%2!=0:
#           print(i)


# #to display  square of 1 to 10 numbers
# for i in range(1,11,1):
#     #  print(i , "square is ",i*i)
#     print(f"{i}  square is {i*i}")

# to dispaly square root of 1 to 10 numbers 
# import math
# for i in range(1,11,1):
#     print(i ,"square root is= ",math.sqrt(i))
# print("5 square root is= ",math.sqrt(5))

# to display multiplication table of a given number
# a=3
# for i in range(1,11):
#     print(a," x ",i," = ",a*i)








