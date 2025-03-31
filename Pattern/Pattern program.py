#Right-Angled Triangle
# Number of rows
rows = 5  

#Loop through the rows
for i in range(1, rows + 1):  
    print("* " * i)  # Print stars with space
'''o/p:
* 
* * 
* * * 
* * * * 
* * * * * 
'''

#Hollow Right-Angled Triangle
# Number of rows
rows = 5  

# Loop through rows
for i in range(1, rows + 1):  
    for j in range(1, i + 1):  
        # Print stars at the boundary
        if j == 1 or j == i or i == rows:  
            print("*", end=" ")  
        else:  
            print(" ", end=" ")  # Print spaces inside
    print()  
'''o/p:
* 
* * 
*   * 
*     * 
* * * * * 
'''

#Inverted Right-Angled Triangle
# Number of rows
rows = 5  

# Loop in reverse
for i in range(rows, 0, -1):  
    print("* " * i)  
'''o/p:
* * * * * 
* * * * 
* * * 
* * 
* 
'''

#Pyramid 
# Number of rows
rows = 5  

# Loop through rows
for i in range(1, rows + 1):  
    # Print leading spaces
    print(" " * (rows - i), end="")  
    # Print stars with space
    print("* " * i)  
'''o/p:
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''

#Diamond
# Number of rows
rows = 4  

# Upper half of the diamond
for i in range(1, rows + 1):  
    print(" " * (rows - i) + "* " * i)  

# Lower half of the diamond
for i in range(rows - 1, 0, -1):  
    print(" " * (rows - i) + "* " * i)  
'''o/p:
   * 
  * * 
 * * * 
* * * * 
 * * * 
  * * 
   * 
'''

#Hollow Diamond
# Number of rows
rows = 5  

# Upper half
for i in range(1, rows + 1):  
    print(" " * (rows - i), end="")  
    for j in range(1, 2 * i):  
        if j == 1 or j == (2 * i - 1):  
            print("*", end="")  
        else:  
            print(" ", end="")  
    print()  

# Lower half
for i in range(rows - 1, 0, -1):  
    print(" " * (rows - i), end="")  
    for j in range(1, 2 * i):  
        if j == 1 or j == (2 * i - 1):  
            print("*", end="")  
        else:  
            print(" ", end="")  
    print()
'''o/p:
    *    
   * *   
  *   *  
 *     * 
*       *
 *     * 
  *   *  
   * *   
    *    
'''

#Number Pattern
# Number of rows
rows = 5  

# Loop through rows
for i in range(1, rows + 1):  
    for j in range(1, i + 1):  
        print(j, end=" ")  # Print numbers in increasing order
    print()  
'''o/p:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

#Floyd's Triangle
# Number of rows
rows = 5  
num = 1  

# Loop through rows
for i in range(1, rows + 1):  
    for j in range(1, i + 1):  
        print(num, end=" ")  # Print the current number
        num += 1  # Increment the number
    print()  
'''o/p:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''

#Hollow Square
# Side length of the square
n = 5  

# Loop through rows
for i in range(n):  
    for j in range(n):  
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:  
            print("*", end=" ")  # Print border stars
        else:  
            print(" ", end=" ")  # Print spaces inside
    print()
'''o/p:
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''

#Butterfly Pattern
# Number of rows
rows = 5  

# Upper half
for i in range(1, rows + 1):  
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)  

# Lower half
for i in range(rows, 0, -1):  
    print("*" * i + " " * (2 * (rows - i)) + "*" * i)
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

#Heart Shape Pattern
# Heart shape dimensions
for row in range(6):  
    for col in range(7):  
        # Print stars at the edges and curves
        if (row == 0 and col % 3 != 0) or \
           (row == 1 and col % 3 == 0) or \
           (row - col == 2) or (row + col == 8):  
            print("*", end=" ")  
        else:  
            print(" ", end=" ")  
    print()
'''o/p:
  * *   * *   
*     *     * 
*           * 
  *       *   
    *   *     
      *       
'''

#Hourglass Pattern
# Number of rows
rows = 5  

# Upper half
for i in range(rows, 0, -1):  
    print(" " * (rows - i) + "* " * i)  

# Lower half
for i in range(2, rows + 1):  
    print(" " * (rows - i) + "* " * i)
'''o/p:
* * * * * 
 * * * *  
  * * *   
   * *    
    *     
   * *    
  * * *   
 * * * *  
* * * * * 
'''