# Topics covered Variables, number and string
# Variables

firstname = "Mahantesh"
rollno = 401115
height = 5.3

print(firstname)
print(rollno)
print(height)

# Data types
print("")
print(type(firstname))
print(type(rollno))
print(type(height))

# Type casting
print("")
a = 20
b= 5.9
firstname1 = "10"
print(a+b)
print(a+int(b))

#print( a + int(firstname))  # invalid casting
print( a + int(firstname1))  # valid casting

print("")
a=10
b=20
print(str(a) + " " + str(b))

print("")
a= "10"
b="20"
print(a + " " + b)

print("")
name = " etlqalabs "
print(10*name) # print names 10 times

# Escape sequence

name1 = " etlqalab1 "
name2 = " etlqalab2 "

print ("")
print(name1)
print(name2)

print("")
print(name1, end = "\n")
print(name2)

print("")
print(name1, end = "")
print(name2)


print("")
print(name1, end = "\t")
print(name2)


