# Used to store multiple items in a variable.

# colours = ("Red","Yellow","Green","Violet","Black","White")

# Properties of Tuples
# Ordered
colours = ("Red","Yellow","Green","Violet","Black","Red",1.23,123,"White",False)
print(colours)

# Immutable(major difference)
# colours[1] = "Grey"
# Above line will throw TypeError: 'tuple' object does not support item assignment

# Duplicacy
# Heterogeneity

# to create a tuple with 1 element only

brands = ("Monte-Carlo")

print(type(brands)) # prints <class 'str'>

# but we wanted to create a tuple so we can add a ',' at last as below

brands = ("Monte-Carlo",)
print(brands)
brands = tuple(("Monte-Carlo","TeamSpirit","Denim","NetPlay"))

print(brands)

print(type(brands)) # prints <class 'tuple'>

print(len(brands)) # prints 1


# Accessing items of the tuple

print(brands[1]) # prints TeamSpirit

# this also supports -ve indexing
print(brands[-1])
# this also supports range indexing
print(brands[0:2])

# To check if a item is present or not

if "London-Jeans" in brands :
    print("We have London-Jeans")

else :
    print("We do not have London-Jeans")

# Traversing the tuple

for i in brands :
    print(i)

# We can concatenate like tuple

# Unpacking a tuple

brand1, brand2, brand3, brand4 = brands

print()
print(brand1)
print(brand2)
print(brand3)
print(brand4)
print()


# Why tuple over a list ?

# Iterating through a 'tuple' is faster than in a 'list'.

# 'Lists' are mutable whereas 'tuples' are immutable. 

# 'Tuples' that contain immutable elements can be used as a key for a dictionary

# reversing a tuple

# creating a new tuple for reversed order

list = []

print(type(list))

for i in reversed(brands) :
    list.append(i)

revTuple = tuple(list)    

print(type(revTuple))
print(revTuple)

# Adding two tuples

tup1 = (1,2,3,4)
tup2 = ("John","Micheal")

tup3 = tup1 + tup2
print(tup3)
print(type(tup3))






