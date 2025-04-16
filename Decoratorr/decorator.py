'''Decorators- it provides additional information to it

Types:
Build in decorators
user defined decorators

one function is parameter of another function- call back function'''

def deco(printer):
    def inner():
        printer()
        print("The Kiran Academy")
        print("The Kiran Academy")
        print("The Kiran Academy")
    return inner

@deco
def printer():
        print("The Kiran Academy")
        print("The Kiran Academy")
printer()

