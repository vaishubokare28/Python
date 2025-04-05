'''exceptional handling

syntax-
try: #try block throw error
  pass
except: #except block handle the error
  pass
finally: #finally block always get executed
  pass
    '''

# a=20
# b=0
# try:
#   div=a/b
# except:
#   print("number is divisible by zero")


# a=20
# b=0
# try:
#   div=a/b
# except Exception as e:
#   print(f"{e}")



# try:
#   print("hello"+5)
# except Exception as e:
#   print(f"{e}")

#if there is exception in try block then except block will be run
#if there is no exception in try block then lese block will be run

# a=20
# b=0
# try:
#   div=a/b
# except Exception as e:
#   print(f"{e}")
# else:
#   print(div)


# a=10
# b=2

# if b!=0:
#     div=(a/b)
#     print(div)
# else:
#     print("division by zero")


# a=20
# b=0
# try:
#   div=a/b
# except Exception as e:
#   print(f"{e}")
# else:
#   print(div)
# finally:
#    print("it if finally block")


# a=20
# b=2
# try:
#   div=a/b
# except Exception as e:
#   print("error")
# except ZeroDivisionError as e:
#   print("zero division error")
# except ValueError as e:
#   print("value error")


#FileNotFound
try:
  f=open("demo.txt","r")
  print(f.read())
  f.close
except FileNotFoundError:
  print("filenotfound...")
