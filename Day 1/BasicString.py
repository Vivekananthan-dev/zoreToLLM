# it Includes the basic string operations also called a Methods in python

str = "Hello world"

# 1. String Length
print(len(str))  # output: 11


# 2. Find the Index of the character in a string
print(str.find("o")) # output: 4
print(str.index("o") ) # output: 4


# 3. Uppercase and Lowercase
print(str.upper())  # output: HELLO WORLD
print(str.lower())  # output: hello world

# 4. Find a the string is number or not
print(str.isdigit())    # output: False
a = "123"
print(a.isdigit())   # output: True

# 5. Check the string is alphanumeric or not
print(str.isalnum())  # output: False
print(a.isalnum())  # output: True

# 6. Check the string is alphabetic or not
print(str.isalpha())  # output: False

## what why it is false because it contains space

rstr = "Helloworld"
print(rstr.isalpha())  # output: True
print(rstr.isalnum())  # output: True

# 7. Check the string is space or not
print(str.isspace())  # output: False
print(" ".isspace())  # output: True

# 8. Check the string is title or not
print(str.istitle())  # output: False
t= "Hello World"
print(t.istitle())  # output: True
## why ? beacause it contains the first letter of each word is capitalized which is the condition of title

# string Slicing means create a substring by extracting element fromanother String

#               indexing[] or slice() [start:stop:step]

sampleSample = "Hello world"
print(sampleSample[0:5])  # output: Hello set start from 0 to 5
print(sampleSample[0:5:2])  # output: Hlo set start from 0 to 5 with step of 2
print(sampleSample[0:5:1])  # output: Hello
print(sampleSample[0:5:3])  # output: Hl

print(sampleSample[6:]) #output: world
print(sampleSample[:5])  #output: Hello

print(sampleSample[::-1])  #output: dlrow olleH reverse the string  beacouse negative  indexing move from right to left
print(sampleSample[::-2])  #output: drwolH

# Slice() method it is simular to indexing but it is more flexible
# it is used to extract a part of the string
# it takes three arguments start, stop and step
# start: the starting index of the slice
# stop: the ending index of the slice
# step: the step size of the slice
# it is optional and default value is 1


web = "www.google.com"
sl = slice(4,-4)
print(web[sl])  #output: google
web2 = "www.HackerRank.com"
print(web2[sl])  #output: HackerRank