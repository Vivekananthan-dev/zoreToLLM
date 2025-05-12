# In python creating a function is simple 
#  function is a block of code that only runs when it is called
#  function can take parameters and return a value
#  function can be called multiple times

# def function_name(parameters):
#     function body
#     return value

def mul(a,b):
    return a*b

def add(a,b):
    c = a+b
    return c

print(mul(2,3))

print(add(2,3))

#keyword arguments
def name(firstname, lastname):
    print("Hello " + firstname + " " + lastname)

name(lastname = "ananthan", firstname = "vivek") # output: Hello vivek ananthan

# *args
# *args is used  to pass many arguments to a function

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5)) # output: 15 # You add even more arguments 

# Not only args we can use any name for it

#**kwargs are used to pass keyword arguments to a function
def student(**kwargs):
    for key, value in kwargs.items():
        print(key + " : " + value)

student(name = "vivek", age = "21", city = "S") # output: name : vivek age : 21 city : S

# lambda function
# lambda function is a small anonymous function
# it can take any number of arguments but can only have one expression
# it is used to create small functions that are not bound to a name

b = lambda x: x + 1
print(b(2)) # output: 3

