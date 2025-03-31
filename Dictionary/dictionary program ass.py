#Q.1)Convert the lists into a dictionary

l1=['name','age','adress']
l2=['Archana',21,'Sangli']

#zip method is available in python for the converting list to dictionary
dict1=dict(zip(l1,l2)) #here  Zip function will consider the l1 as l1=>keys and l2 as a l2=>values
print(dict1)
print(type(dict1))
{'name': 'Archana', 'age': 21, 'adress': 'Sangli'}

#o/p
# <class 'dict'>


#Q.2)Merge two python dictionaries into one

d1={'name':'Archana','age':21,'adress':'Sangli'}
d2={'Contact No':123,'College':'Pvpit','Stream':'Engineering'}

d1.update(d2)
print("This is merged dictionary: ",d1)

#o/p
#This is merged dictionary:  {'name': 'Archana', 'age': 21, 'adress': 'Sangli', 'Contact No': 123, 'College': 'Pvpit', 'Stream': 'Engineering'}


#Q.3)initialize dictionary with default values

d1=['a','b','c']
default_value=0

#this is method1 using loop
my_dict={}
for i in d1:
    my_dict[i]=default_value
print("this is 1st method: ",my_dict)  

#method2 - using dictionary comprehension
my_dict1={i:default_value for i in d1}
print("this is 2nd method: ",my_dict1)

# o/p
# this is 1st method:  {'a': 0, 'b': 0, 'c': 0}
# this is 2nd method:  {'a': 0, 'b': 0, 'c': 0}

#Q.4)print the value of key as 'history' from the below dict

dict={'sub1':'hindi','sub2':'english','sub3':'history','sub4':'maths'}
#method 1
print(dict['sub3'])

#method2 using for loop
for key, value in dict.items():
    if value=='history':
        print(value)

# history
# history

#Q.5)create a dictionary by extracting the keys from a given dictionary

d1={'name':'Archana','age':21,'adress':'Sangli'}
keys_extract=['name','age'] #keys that want to extract
new_dict={} #make empty dictionary

for key, value in d1.items(): # to extract the values in d1.items()
    if key in keys_extract:
        new_dict[key]=value
print(new_dict)        
#o/p
#{'name': 'Archana', 'age': 21}

#Q.6)delete the list of keys from a dictionary

dict={'sub1':'hindi','sub2':'english','sub3':'history','sub4':'maths'}
removable_keys=['sub1','sub2']

for i in removable_keys: # if i(keys) are present in dict which are mentioned in removable_keys
    if i in dict:        #if yes then delete it from the dict
        del dict[i]        
print(dict)

#o/p
#{'sub3': 'history', 'sub4': 'maths'}

#Q.7)check if value exist in dictionary
d1={'name':'Archana','age':21,'adress':'Sangli'}

if 'Archana' in d1.values():
    print("yes")
else:
    print("No")
#o/p
#yes


#Q.8)rename key from a dictionary

d1={'name':'Archana','age':21,'adress':'Sangli'}

#we can rename the key
d1['Student Name']=d1.pop('name')
print(d1)
#o/p
#{'age': 21, 'adress': 'Sangli', 'Student Name': 'Archana'}

#Q.9)get the key of minimum value from a given dictionary

dict={'marks1':77,'marks2':90,'marks3':34,'marks4':67}

min_value=min(dict.values())
print(min_value)

#o/p
#34
#Q.10)change the value of key in nested dictionary

cars = {
    "car1": {
        "TATA_Company": {
            "Vagnor": {
                "price": "40L",
                "seating capacity": 6,
                "color": "maroon",
                "fuel_type": "oil"
            },
            "Honda": {
                "price": 560000,
                "seating capacity": 8,
                "color": "blue",
                "fuel_type": "engine_oil"
            }
        }
    },
    "car2": {
        "Mahindra and Mahindra": {
            "price": 568897,
            "color": "blue",
            "model_no": "brand1",
            "seating capacity": 6
        },
        "Maruti": {
            "price": 568897,
            "color": "blue",
            "model_no": "brand2",
            "seating capacity": 6
        }
    }
}

#to change the name of key TATA_company to TATA cars
cars["car1"]["TATA Cars"]=cars["car1"].pop("TATA_Company")
print(cars)

#o/p
#{'car1': {'TATA Cars': {'Vagnor': {'price': '40L', 'seating capacity': 6, 'color': 'maroon', 'fuel_type': 'oil'}, 
# 'Honda': {'price': 560000, 'seating capacity': 8, 'color': 'blue', 'fuel_type': 'engine_oil'}}}, 
# 'car2': {'Mahindra and Mahindra': {'price': 568897, 'color': 'blue', 'model_no': 'brand1', 'seating capacity': 6},
#  'Maruti': {'price': 568897, 'color': 'blue', 'model_no': 'brand2', 'seating capacity': 6}}}