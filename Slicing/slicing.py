# # name="Instagram"
# # print(name[0:4]) #Inst
# # print(name[3:8] )#tagra
# # print(name[5: ]) #gram
# # print(name[0: :2]) #Isarm

# # #reverse string
# # print(name[:: -1])  #margatsnI

# # print(name[-9:-5]) #Inst
# # print(name[-6::-1])#tsnI

# # print(name[-4: ]) #gram
# # print(name[-9: :2 ]) #Isarm


# #1)to check string is palindrome or not
# str="python"
# rev=str[::-1]   #nohtyp

# if (str == rev):
#     print("String is palindrome")
# else:
#     print("string is not palindrome")

# #2)To calculate length of the string without using len() 
# name="Instagram"
# length=0
# for i in name:
#     length=length+1
# print("length of string=",length)  #length of string= 9

# #3)To display reverse string
# name="Instagram"
# l=len(name)-1  #len(name)= 9-1=8 
# for i in range(l,-1,-1):
#     print(name[i],end="")

# name= "Instagram"
# rev = ""               #
# for i in name:
#    rev = i+rev   #rev=  margatsnI
# print(rev)    
    
# #4)to check string is palindrome or not  without using [::-1] 
# string=input("Enter string ")
# l=len(string)-1
# rev=""
# for i in range(l,-1,-1):
#    rev=rev+string[i]
# print(rev)

# if string==rev:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")


# num = input("Enter your number :")
# r_num = ""
# for i in range (len(num)-1,-1,-1):
#     r_num += num[i]

# if num == r_num:
#       print("Number is Palindrome")
# else:
#        print("Number is not Palindrome")


# string=input("Enter string ")
# l=len(string)-1
# rev=""
# for i in string:
#     rev= i+rev
# if string==rev:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")


str="amruta"
print(sorted(str)) #['a', 'a', 'm', 'r', 't', 'u']

#1.to check string is anagram or not
str1="silent"   "amruta"
str2="listen"    "tampru"

#2.to check enter password and confirm password is equal or not
password="pass@1234"
confirm_password="pass@3456"

#3.To count  number of alphabets, count no of digits,count no of spaces ,count no of special symbols
password="pass@12 34"









