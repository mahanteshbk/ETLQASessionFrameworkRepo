# Topics covered are
# Set, Dictionary

# Collections objects/ data types
# List []  - can have duplicate values
# Tuples ()
# Set {} - No have duplicate values, no sorting, sorted based on hash values
# Dictionaries {}

list1 = ['apple','banana','orange', 'apple']
print(list1)

list1.append('mango')  # append will add values at the list end
print(list1)

set1 = {'apple','banana','orange', 'apple'} # eliminates duplicates
print("")
print(set1)
set1.add('mango')
print(set1)

# Set attributes:- union
print("")
s1 = {'apple','banana','orange'}
s2 = {'apple','banana','guava'}
s3= s1.union(s2)
print(s3)

s4 = s1.intersection(s2)
print(s4)



# Dictionaries  - KEY VALUE PAIR

dict1 = {1:"Virat", 2:"Rohit"}
print("")
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
print(dict1[2])

# add values to dict

dict1[3]= "Rahul"
print(dict1)


# create empty set, dict, list, tuples

l = []
t = ()
s = set() # for empty set
d = {}
s1 = {}
print("")
print(type(l))
print(type(t))
print(type(s))
print(type(d))
print(type(s1))
