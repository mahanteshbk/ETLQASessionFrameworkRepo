# find the duplicates from the list


l = [1,2,3,5,8,10,2,8,12,5]

d = {}
print("******")

# put all values in dict and the number of occurrences
for item in l:
    if item in d:
        d[item] = d.get(item)+1
    else:
        d[item] = 1
print(d)

# print only the duplicate values
for element in d:
    if d.get(element)>1:
        print(element)
