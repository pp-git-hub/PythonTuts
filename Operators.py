# Logical Operators in Python

# and, or, not

# Relational Operators 
# <, <=, >, >=, !=, ==,

exp1 = 2 > 1
exp2 = 5 < 4
exp3 = 5 == 5

print(exp3)

print(exp1 and exp2)
print(exp1 or exp2)
print(not(exp2))

# Identity Operators

# is, is not (for objects)

x = 5
y = 5

print("if x is y : ", x is y)
print("if x is not y : ", x is not y)

# membership operators

# in, not in

fruits = ["apple","banana","cherry"]

print("if banana is present in fruits : ", "banana" in fruits)
print("if grapes in fruits : ", "grapes" in fruits)

# Bitwise operators

# &, |, ^, ~, <<, >>

# Works on Binary digits

print(22 << 1)
print(22 >> 1)
print(5 & 3)
print(5 | 3)
print(5 ^ 3)