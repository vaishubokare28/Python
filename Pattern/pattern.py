for i in range(1, 6):  # Row loop (outer loop)
    for j in range(1, 6):  # Column loop (inner loop)
        print("*", end=" ")  # Print '*' and stay on the same line
    print(" ", end="\n")  # Move to the next line after completing one row
'''o/p: 
* * * * *  
* * * * *  
* * * * *
* * * * *
* * * * *
'''


for i in range(1, 6):  
    for j in range(1, 6):  
        print(i, end=" ") 
    print(" ", end="\n")
'''o/p:
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
'''


for i in range(1, 6):  
    for j in range(1, 6):  
        print(j, end=" ") 
    print(" ", end="\n")
'''o/p:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''


for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("",end="\n")  
'''o/p:
* * * * *
*       *
*       *
*       *
* * * * *
'''


for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ",end="\n")
'''o/p:
*
* *
* * *
* * * *
* * * * *
'''


for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ",end="\n")
'''o/p:
1
1 2
1 2 3
1 2 3 4  
1 2 3 4 5
'''



for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ",end="\n")
'''o/p:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''


for i in range(1,6):
    for j in range(1,i+1):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print(" ",end="\n")
'''o/p:
0
0 1
0 1 0
0 1 0 1
0 1 0 1 0
'''


for i in range(1,6):
    for j in range(1,i+1):
        if (i%2!=0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print(" ",end="\n")
'''o/p:
1
0 0
1 1 1
0 0 0 0
1 1 1 1 1
'''


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
'''o/p:
A
B B
C C C
D D D D
E E E E E
'''


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
'''o/p:
A
A B
A B C
A B C D
A B C D E
'''


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
'''o/p:
E E E E E
D D D D
C C C
B B
A
'''


for i in range(5,0,-1):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()
'''o/p:
A B C D E
A B C D
A B C 
A B
A
'''


n=int(input("Enter pattern number:"))
for i in range(n,0,-1): #upper
    for k in range(1,i+1): #left side
        print("*",end=" ")
    for j in range(0,2*(n-i)): #spaces
        print(" ",end=" ")
    for l in range(i):   #right side
        print("*",end=" ")
    print()
for i in range(2,n+1):  #lower
    for p in range(1,i+1): #left side
        print("*",end=" ")
    for q in range(1,((n-i)*2)+1): #space
        print(" ",end=" ")
    for r in range(i):   #right side
        print("*",end=" ")
    print()
'''o/p:
* * * * * * * * * * 
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
'''
        #OR
# Lower half first (in reverse order)
for i in range(5, 0, -1):
    print("*" * i + " " * (2 * (5 - i)) + "*" * i)

# Upper half
for i in range(1, 6):
    print("*" * i + " " * (2 * (5 - i)) + "*" * i)

'''O/P:
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''

#Butterfly Pattern
# Upper half of the butterfly
for i in range(1, 6):
    print("*" * i + " " * (2 * (5 - i)) + "*" * i)

# Lower half of the butterfly
for i in range(5, 0, -1):
    print("*" * i + " " * (2 * (5 - i)) + "*" * i)
'''o/p:
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
'''

 
    
    