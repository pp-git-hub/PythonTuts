# greatest of 3 integers using ternary operator

a = int(input("Please enter 1st number : "))
b = int(input("Please enter 2nd number : "))
c = int(input("Please enter 3rd number : "))

greatest = a if a > b and a > c else b if b > c else c

print("The greatest number is ", greatest)

