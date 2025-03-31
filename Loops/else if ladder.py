'''else if ladder'''

#accept 3 numbers and display greater no among 3 number
a=input("Enter value of a:")
b=input("Enter value of b:")
c=input("Enter value of c:")

if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
else:
    print("c is greater")

#accept 3 subject and sum and percentage
sub1=int(input("Enter marks of sub1:"))
sub2=int(input("Enter marks of sub2:"))
sub3=int(input("Enter marks of sub3:"))

sum=sub1+sub2+sub3
print(sum)

per=(sum/300)*100
print(per)

if per>=75:
    print("Distinction")
elif per>=60:
    print("First class")
elif per>=50:
    print("Second class")
elif per>= 40:
    print("Pass")
else:
    print("Fail")