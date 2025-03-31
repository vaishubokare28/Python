
# display factorial of given number
num=int(input("enter no."))
mul=1
for i in range(1,num+1):
     mul=mul*i
print("mul=" ,mul)


# dispaly square of 1 to 10 numbers
for i in range(1, 11):
    print("square of",i," = ", i**2)



# accept any city from the user and display monument of that city
# city              monument
# delhi             red fort
# agra              taj mahal
# jaipur            jai mahal
city=str(input("Enter city name:"))
if city=="delhi":
    print("Red Fort")
elif city=="agra":
    print("Taj Mahal")
elif city=="jaipur":
    print("Jai Mahal")
else:
    print("None...")


# accept the cost price of a bike and display the raod tax to be paid according to the following criteria:
# cost price(in rs)                     tax
# >100000                               15%
# >50000 and <=100000                   10%
# <=50000                               5%
cost = int(input("Enter cost price of bike: "))

if cost > 100000:
    tax = 0.15 * cost
    print("15% road tax to be paid:" ,tax)
elif cost > 50000 and cost <=100000:
    tax = 0.10 * cost
    print("10% road tax to be paid:" ,tax)
else:
    tax = 0.05 * cost
    print("5% road tax to be paid:", tax)


#calculate electricity bill(accept number of units from users according to following criteria)
#unit                              price
#first 100 units                no charge
#next 100 units              rs.5 per unit
#after 200 units             rs.10 per unit
electricity_bill=0
units=int(input("Enter the units you have used:"))
if units<=100:
    print("No chatges")
elif units<=200:
    electricity_bill=(units-100)*5
    print("Charges on units is:")
else:
    electricity_bill=((100*0)+(100*5)+((units-200)*10))
    print("Total electricity bill is:" , electricity_bill)