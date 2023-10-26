# string 
name = "Isha"

#Integer
roll_number = 17

# floating number
percentage = 95.8

# boolean
is_student = True

# character 
gender = 'M'

print(name)
print(roll_number)
print(percentage)
print(is_student)
print(gender)

# printing in one line



percentage = 94.4

# same variable get updated
print(name, roll_number, percentage, is_student, gender)


# printing type of the variable

print(name, roll_number, percentage, is_student, gender)
print(type(name),type(roll_number),type(percentage),type(is_student),type(gender))


myname = "Pranjal Pandey"
print("My Name is " + myname + " and my roll number is ", roll_number)

# we can't concatenate two different data types

# but we can we use ',' in print function

print("My percentage has changed to ", percentage + 1.0)

# print with separator

print(name, roll_number, percentage, is_student, gender, sep = " - ")

print("Fibonacci Series is 0 : ", 1,1,2,3,5,8,13,21, "....", sep = ",")

# Data Types in Python

# Numeric : Int, Float, Complex
# Text : String ('' or "")
# Boolean : (True or False)
# Sequence : List[], Tuple() (of diff data types)
# Mapping : Dictionary(key-value pairs){} , set {}(unordered collection of unique data type)
# Nothing : None (like Null)

# ASCII and UNICODE values

# 'A' to 'Z' -> 65 to 90
#  'a' to 'z' -> 97 to 122
#  48 to 57 -> 0 to 9
#  32 -> space

# to print ascii value of passed character 

print(ord(' '))

