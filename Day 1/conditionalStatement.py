# All Conditional Statements
# 1. if statement : a block of code that will be executed if it's condition is true
a =  10
if a<5:
    print("a is less than 5")
# In most of the language we use curly braces to define the block of code but in python we use indentation

if a>5:
    print("a is greater than 5") #output: a is greater than 5

# 2. if else statement : if block need condition to check but else won't need any condition
# Else will be executed if the condition of if statement is false 
if a<5:
    print("a is less than 5")
else:
    print("a is greater than 5")# output: a is greater than 5

# 3. if elif else statement:  elif is used to check multiple conditions
x=2
y=4
z=6
if x>y and x>z:
    print("x is greater than y and z")
elif y>x and y>z:
    print("y is greater than x and z")
elif z>x and z>y:
    print("z is greater than x and y")
else:
    print("x,y and z are equal") # output: z is greater than x and y
    
# 4. Nested if statement 
# Nested if is used to check the condition inside the if block

if x<y:
    print("x is less than y")
    if x<z:
        print("x is less than z") # output: x is less than y
    else:
        print("x is greater than z")

## looping statement 
# while loop
# while loop is used to execute a block of code as long as the condition is true
i= True 
j = True
while i and j:
    print("Hello world")
    i = False

while i or j:
    print("2. Hello world")
    i = False
    j = False

while not(i and j):
    print("3. Hello world")
    i = True
    j = True

# its the logical operator and how to use in python
# where while loop is nothing different then other language for loop does have difference
# for loop
# for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string)

# Before that will see how to read value from user in pythoon first
# input() function is used to take input from the user
# it takes one argument which is the prompt string
# it is optional and default value is empty string
# it returns the value entered by the user as a string

v = int(input("Enter a number: ")) #By default it will take the input as string to covert we have to convert it.

print(v) #output: 5

for s in range(v):
    print(s) #output: 0 1 2 3 4

for s in range(1, v): # it will start from 1 to v-1
    print(s) #output: 1 2 3 4

for s in range(1, v, 2): # it will start from 1 to v-1 with step of 2
    print(s) #output: 1 3
for s in range(1, v, 3): # it will start from 1 to v-1 with step of 3
    print(s) #output: 1 4

#let's see some features

for s in "Hello":
    print(s) #output: H e l l o
# it will iterate over the string and print each character

# will make a for loop with time delay

import time

for s in range(10,0,-1):
    print(s)
   # time.sleep(1) # it will wait for 1 second before printing the next number   

print("happy programming")
# it will print the countdown from 10 to 0 with a delay of 1 second

# for loop with else statement
# else statement will be executed if the for loop is not terminated by break statement
for s in range(5):
    print(s)
else:
    print("for loop is completed")

# its time for nested loop
# nested loop is used to iterate over a sequence inside another loop

for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

# since their is no do while loop in python
# we can use while loop to achieve the same by creating a condition inside the loop
