'''Dictionary
1. comma sep key:value pair within {}
2. dict_name={key1:value1 , key2:value2}
3. key can not be duplicate -- immutable , but value can be duplicate -- mutable or immutable)
4.
'''

student={"Roll_no":1 , "Name":"Riya" , "Age":20 , "City":"Pune"}
print(student)
print(type(student))
print(student["Roll_no"]) #by using key we can access value

#dictionary contains list
number={"even":[2,4,6,8,10] , "odd":[1,3,5,7,9]}
print(number)
print(number["even"])
print(number["odd"])

#how to create Nested dictionary
mobile={"Apple":{"iphone5":{"camera":"15mp" , "ram":"4gb"} , 
                 "iphone6":{"camera":"12mp" , "ram":"6gb"}} , 
        "Vivo":{"vivo v7":{"camera":"24mp" , "ram":"4gb"} , 
                "vivo v9":{"camera":"16mp" , "ram":"4"}}}
print(mobile)

#create a dictionary of car
car1={"model":"tata",
      "color":"black", 
      "price":"7.66lakh"}
print(car1)

car2={"tata":
            {"model":"punch",
             "color":"black", 
             "price":"7.66lakh"},
      "Maruti suzuki":
            {"model":"Swift",
             "color":"white", 
             "price":"6.49lakh"}}
print(car2)
print(car2["tata"])
print(car2["tata"]["model"])

car3={"tata":
            {"punch":{
             "color":"black", 
             "price":"7.66lakh"}},
      "Maruti suzuki":
            {"Swift":{
             "color":"white", 
             "price":"6.49lakh"}}}
print(car3)
print(car3["tata"])
print(car3["tata"]["punch"])
print(car3["tata"]["punch"]["color"])


#how to add and update data in dictionary
student1={"Roll_no":1 , "Name":"Riya" , "Age":20 , "City":"Pune"}
'''var['key']=value'''

student1["phone_no"]=9087456329
print(student1) #add value

student1["Roll_no"]=2 
print(student1) #update value


student2={}
student2["Name"]="Shyam"
print(student2) #add key:value pair to empty dictionary

'''dictionary methods
1. keys()
2. values()
3. itmes()
'''

'''keys() - it return list of keys'''
student3={"Roll_no":1 , "Name":"Riya" , "Age":20 , "City":"Pune"}
print(student3.keys())

#values() - it return list of values
student3={"Roll_no":1 , "Name":"Riya" , "Age":20 , "City":"Pune"}
print(student3.values())

#items() - it return list of tuple key:value pair
student3={"Roll_no":1 , "Name":"Riya" , "Age":20 , "City":"Pune"}
print(student3.items())

student3={"Roll_no":1 , "Name":"Riya" , "Age":20 , "City":"Pune"}
for i in student3:
    print(i)

for i in student3.keys():
    print(i)

for i in student3.values():
    print(i)

for i in student3.items():
    print(i) 

