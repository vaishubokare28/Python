#1.draw diamond 
n = int(input("Enter a number:"))
# upper part of diamond
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))                 
# lower part of diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))                


#2.display a numbers and its squares in dictionary
square={i:i**2 for i in range(1,6)}
print(square)

sq = {}
for i in range(1, 6):
    sq[i] = i ** 2  
print(sq)

#3.check given number is armstrong number or not
num=int(input("Enter a number:"))
num_str=str(num)
num_digits=len(num_str)  

sum_of_powers=sum(int(digit)**num_digits for digit in num_str )
if sum_of_powers == num:
    print(f"{num} is an Armstrong number")  
else:
    print(f"{num} is Not an Armstrong number")  



















































# upper part of diamond
#5-0-1=4    2*0+1=1
#5-1-1=3    2*1+1=3
#5-2-1=2    2*2+1=5
#5-3-1=1    2*3+1=7
#5-4-1=0    2*4+1=9

# lower part of diamond
# 5-0-1=4    2 * i + 1


