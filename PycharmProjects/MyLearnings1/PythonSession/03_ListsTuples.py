# Topics covered:-
# String Index, length,
# Lists, insert sort and Tuples

mystr = "This is a string variable"
print(mystr[0]) # first character
print(mystr[0:4]) # first 4 char

print("")
print(mystr[0:25:2])  # jumping 2 char
print(mystr[0:25:3])  # jumping 3 char

print("")
print(len(mystr))  # length

# LISTS

fruits = ['apple', 'banana', 'orange', 2] # list can have any data types
print("")
print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[-2])
print(fruits[0:2])
print(fruits[0:4])

# Mutable - which can be changed
# and immutable - canot be changed

fruits1 = ['apple', 'banana', 'orange']
fruits1.insert(1,"Mango")
print("")
print(fruits1)
fruits1.sort()
print(fruits1)
fruits1.reverse()
print(fruits1)

# TUPLES  -- immutable

fruits2 = ['apple', 'banana', 'orange']
print("")
print(fruits2)
fruits2.sort()
print(fruits2)
fruits2.reverse()
print(fruits2)






