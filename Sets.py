# Set is a container used for storing multiple values in a variable

institutes = {"ABES","NITW","NITK","NITA"}

# Properties of set

# Unordered
# Immutable
# Unindexed
# No Duplicacy
# Heteogeneity

numbers = {1,2,3,3,-1,-4,-34,0,11,456,230,111,241,1,0,1,0,0,13,345,222,45,23,22,1,3,4,2}
print(numbers)

print(len(numbers))
print(type(numbers))

# to access and print set elements 
# we are using loop because there is no indexing concept in sets

for i in numbers :
    print(i)

# To check if a item exists in a set

if 1000 in numbers :
    print("1000 is Present")

else :
    print("1000 is Absent")

# adding element to a set
numbers.add(1000)

print(numbers)


# To add another sequence to the set

prime_numbers = [2,3,5,7,11]
print(id(numbers))
numbers.update(prime_numbers)


print(numbers)

print(type(numbers))

print(""" 
      Nandkishore Kuwar Hari Natwar,
      Baanke Bihari Govinda Giridhar,
      Keshav Madhav Shyam Murari,
      Natwar Nat Nagar Girdhari

      Hari Sukh Karta,
      Hari Dukh Harta
      Hari Hari Har Naam Japna,
      Hare Krishna ,Hare Krishna
      Krishna Krishna Hare Hare
      Hare Rama Hare Rama,
      Rama Rama Hare Hare
""")


numbers.remove(-34)
print(numbers)

# Below function will not throw an error in case when value is absent 
numbers.discard(-34)

# joining two sets

s1 = {1,2,3,4}
s2 = {2,8,9}

s3 = s1.union(s2)

print(s3)

s1.update(s2) # Another way of Joining two sets

# Keep only duplicates while joining

s1.intersection_update(s2)

print(s1)

# keep all values except duplicates

s1.symmetric_difference_update(s3)

print(s1)

print("Minimum Element : ", min(s1))
print("Maximum Element : ", max(s1))



