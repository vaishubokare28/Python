#write a python program to sum all the items in a dictionary

marks={'sub1':67,'sub2':56,'sub3':45,'sub4':77}

sum=0
for i in marks.values():
    sum=sum+i
print(marks.values())
print("Total marks is: ",sum)


#write a python program to all multiply the items in a dictionary

dic={'sub1':7,'sub2':6,'sub3':4,'sub4':5}

mul=1
for i in dic.values():
    mul=mul*i
print(mul)    

#write a python program to convert two lists into dictionary

l1=["one","two","three","four","five"]
l2=[1,2,3,4,5]
 #we have to use zip function -zip(keys,values)=>zip(l1,l2)
result=dict(zip(l1,l2))
print(result)


#write a python script to print dictionary where the keys are numbers between 1 and n(both included) and the values are square of keys

#output expected -{1:1,2:4,3:9,4:16,5:25}

n=int(input("enter the value of n: "))
dict1={}
for i in range(1,n+1):
    dict1[i]=i**2
print(dict1)

#write a python script to merge two python dictionaries
#sample output
#{'name':"ram","age":23}
#{"city":"salem","gender":"male"}

d1={'name':"ram","age":23}
d2={"city":"salem","gender":"male"}
d1.update(d2)
print(d1)


#display Maximun and Minimum Values

marks={'sub1':67,'sub2':56,"sub3":45,"sub4":77}

print("maximum number is",(max(marks.values())))
print("minimum number is",(min(marks.values())))

#to display subjects who's marks is greater than 60

d={}
for subject,score in marks.items():
    if score>60:
       # print(subject,":",score)
        l={subject:score}
        d.update(l)
print(d)       

#to display students who lives in pune
emp={'jonh':'mumbai','blake':'pune','tiger':'delhi','joe':'pune'}
e={}
for name,city in emp.items():
    if city=='pune':
        l={name:city}
        e.update(l)
print(e)        


#write the python program to filter the height and weight of students, which are stored in a dictionary
# original dictionary:
# {'cieera vega':(6.2,70),'alden cantrell':(5.9,65),'kierra Gentry':(6.0,68),'Pierre Cox':(5.8,66)}
# output-
# height>6ft and weight>70 kg:
# {'cierra vega':(6.2,70)}

d={'cieera vega':(6.2,70),'alden cantrell':(5.9,65),'kierra Gentry':(6.0,68),'Pierre Cox':(5.8,66)}

student={}
for i,j in d.items():
    height,weight=j
    if height>=6 and weight>=70:
        student[i]=j
print(student,"\n")    


#write a python  script to sort (ascending and descending)a dictionary by value.

dict1={'cieera vega':(6.2,70),'alden cantrell':(5.9,65),'kierra Gentry':(6.0,68),'Pierre Cox':(5.8,66)}


sort_asc=dict(sorted(dict1.items()))
sort_asc = dict(sorted(dict1.items()))
print("asecending order: ",sort_asc,"\n")


sort_desc=dict(sorted(dict1.items(),reverse=True))
print("desceding order: ", sort_desc,"\n")

print()


#count of the letters from the string
#str1="welcome to jbk"

str1="welcome to jbk"
count=0
for i in str1.split():
    count=count+1
print("number of words in given string is: ",count)    


#write a python program to get the top three items in shop
#items={'item1':45.50,'item2':35,'item3':41.20,'item4':55,'item5':24}

#output-55,45.50,41.20

items={'item1':45.50,'item2':35,'item3':41.20,'item4':55,'item5':24}

sort_desc1=sorted(items.values(),reverse=True)
print(sort_desc1)
top_ele=sort_desc1[:3]

print("this is top 3 items: ",top_ele)