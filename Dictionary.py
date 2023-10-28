# Key-Value pairs are stored

# Properties of a Dictionary

# Ordered
# Changeable
# Unindexed
# No Duplicacy
# Heterogeneity

# creating a dictionary in Python

student = {
            "22MCF1R33" : "Pranjal Pandey",
            "22MCF1R18" : "Devesh Gupta",
            "22MCF1R27" : "Mukesh Ravidas",
            "22MCF1R33" : "Pranjal Pandey"
          }

# values can be duplicate but keys can't

# values can be boolean, string , float, list...

print(student)
print(type(student))

# Checking type of Dictionary

print(len(student))

# Accessing items of a dictionary

print(student["22MCF1R18"])
# or
print(student.get("22MCF1R18"))

print(student.keys())
print(student.values())

# Update the value

student["22MCF1R18"] = "Devesh"

print(student)

# Add element to the dictionary

student["22MCF1R14"] = "Bhukya Chinna"

print("\n",student)

print(len(student))

# Adding dictionary to a dictionary

moreStudent = {
                 "22MCF1R01" : "Bhalu-Muneem"
              }

student.update(moreStudent)

print(student)

# Remove the last added item

student.popitem()

print(student)

# Remove specific keyed item

student.pop("22MCF1R18")

print(student)

# Looping through the Dictionary Keys

for i in student :
    print(i)

# Looping through the Dictionary Values

for i in student :
    print(student[i])


# Printing Both Together

for i in student.items() :
    print(i)

# Printing Both Separately

for i,j in student.items() :
    print(i,j)

# Nested Dictionaries

pincodes = {
              "UP" : {
                        "Bahraich" : 271801,
                        "Lucknow"  : 226021
                     },

               "TS" : {
                        "Warangal" : 506004,
                        "Hyderabad" : 503403
                      }
           }

# To access and print Warangal's Pincode

print(pincodes["TS"]["Warangal"])

# To find the sum of all values in a dictionary

marks = {
           "English" : 45,
           "Mathematics" : 55,
           "Chemistry" : 65,
           "Physics" : 55
        }

print(sum(marks.values()))