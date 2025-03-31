'''Iterative loop - for
for var_name in range(start,stop,step):
start= bydefault is 1
stop=value-1
step=increment /decrement'''

for i in range(1,11,1):
    print(i)


#display odd number from 1 to 20
for i in range(1,20,2):
    print(i)


#display reverse number 
for i in range(10,0,-1):
    print(i)


#display sum of 1 to 10
sum=0
for i in range(1,11,1):
    sum=sum+i
print("sum=" ,sum)

#dispaly multiplication of 1 to 10
mul=1
for i in range(1,11,1):
    mul=mul*i
print("mul=" ,mul)

#display multiplication table of given number
n=int(input("Enter n="))
for i in range(1,11):
    print(n , "* " , i , "=" , n*i)
    print(f"{n} * {i} = {n*i}")



