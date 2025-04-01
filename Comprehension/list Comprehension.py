# """list Comprehension - used to comprehense list
# Syntax:
# var_name=[expression for variable in sequence]
# """


# l=[1,2,3,4,5]

# sq=[]
# for i in l: #normal method
#     sq.append(i**2)
# print(sq)

# square=[i**2 for i in l] #list Comprehension
# print(square)

# #length
# name=["john","pooja","martin","anuja"]
# length=[len(i) for i in name]
# print(length)

# #convert into uppercase
# name=["john","pooja","martin","anuja"]
# uppr=[i.upper() for i in name]
# print(uppr)

# #display first character fromgiven string
# name=["john","pooja","martin","anuja"]
# ch=[i[0] for i in name]
# print(ch)



# """Syntax:
# var_name=[expression for variable in sequence if condition]"""


# #display even number
# l1=[1,2,3,4,5,6,7,8,9,10]
# even=[i for i in l1 if i%2==0 ]
# print(even)

# #display positive number
# num=[34,-45,67,-11,-20]
# positive=[i for i in num if i>0 ]
# print(positive)

# #display string whose start with vowels
# name=["john","pooja","martin","anuja"]
# vowels=[i for i in name if i[0] in ("a","e","i","o","u")]
# print(vowels)

# #display digit only
# s="amruta123jbk19"
# digit=[i for i in s if i.isdigit() ]
# print(digit)



# """syntax:
# var=[exp1 if condition else exp2 for for var in sequence]"""

# #even no - square and odd number - cube
# l1=[1,2,3,4,5,6,7,8,9,10]
# even=[]
# odd=[]
# for num in l1: #normal form
#     if num%2==0:
#         even.append(num**2)
#     else:
#         odd.append(num**3)
# print(even)
# print(odd)

# l1=[1,2,3,4,5,6,7,8,9,10]
# result=[num**2 if num%2==0 else num**3 for num in l1]
# print(result)


"""Advantages of comprehension-
# 1)less code writing
# 2)faster execution
# 3)improve performance
# 4)easier filterining
# 5)memory efficiency
# 6)Short and Simple Code 
# 7)Faster than Loops
# 8)Easy to Understand
# 9)Less Mistakes
# 10)Memory Friendly
"""


