# variable are reuseable container for storing a value

age = 21
print(age) # It display the value stored in the variable (output: 21)

print("age") #It simply print "age" because every thing within the qoutes('' or "") are consider as string (Output : age)

### Note: print() is a function returns None it works in stream 

a = print("jcsbv")
print(a)#output: None

# To print both variable and a string we use separater ' , ' 

print("My age :", age) #output: (My age : 21) It assume a two string 

#second way to print both string and integer together is by concatenation
print("My age : " + str(age))#output: My age : 21

#in print function the string can be concat with only string

##Third way to do that is using "f-string"

print(f"My age : {age}")# output: My age : 21 the "{}" will act as a placeholder


### DataType 

#integer

i = 2 # numbers without point values 
print(type(i)) #output:<class 'int'>

#float

f = 2.5 # numbers with point values
print(type(f)) #output:<class 'float'>

#String

s = "Hello" #serious  of character where we have to use single or double qoutes ("" or '')
print(type(s)) #output:<class 'str'>
s = s+ "hi"
print(s)#output: Hellohi

#Boolean

b = True # zeros and ones let say True =1 and False = 0
B = False

print(type(b))#output:<class 'bool'>
print(type(B)) #output:<class 'bool'>


## Multiple Assingment

x,y,z = 1,2,3
print(x,y,z) #output: 1 2 3