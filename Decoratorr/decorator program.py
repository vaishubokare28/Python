# #sum of 3 number
def deco(sum):
    def inner():
        res=sum()
        c=int(input("Enter c="))
        return res+c
    return inner

@deco
def sum():
    a=int(input("Enter a="))
    b=int(input("Enter b="))
    result=a+b
    return result
print(sum())


# #muplication of 3 numbers
def deco(mul):
    def inner():
        res=mul()
        c=int(input("Enter c="))
        return res*c
    return inner

@deco
def mul():
    a=int(input("Enter a="))
    b=int(input("Enter b="))
    return a*b
print(mul())

#accept firstname=john lastname=deo to cnvert firastname and lastname to upper by using decorator
def upper(getname):
    def inner():
       res=getname()
       return res.upper()
    return inner


@upper
def getname():
    firstname=input("Enter first name:")
    lastname=input("Enter last name:")
    fullname=firstname+" "+lastname
    return fullname
print(getname())
