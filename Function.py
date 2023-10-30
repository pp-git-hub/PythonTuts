# Built-in, user-defined

# Fucntion to add sum of two numbers

n1 = 2
n2 = 4

def sum(n1 = 3,n2 = 0) : # n2 = 0 is a default argument
    ans = n1 + n2
    return ans

print(sum(n1,n2))

print(sum(2))

print(sum())

# Types of arguments

# Default argument
# keyword Arguments(named arguments)
# Positional arguments
# Arbitrary Arguments

print(sum(n2 = 5,n1 = 4))
# Above is a example of keyword argument

# Below is a example of Arbitrary arguments
# Note that args is a tuple
def addNumbers(*args) :
    sum = 0
    for i in args :
        sum += i
    return sum 

output = addNumbers(1,2,3,4,5)

print(output)

# *args,**kwargs(keyworded arguments)

def studentInfo(**kwargs) :
    for x,y in kwargs.items() :
        print(x ," is ", y)

# kwargs acts as a Dictionary
studentInfo(name  = "Pranjal", age = 22, city = "Delhi")
studentInfo(name  = "Karna", age = 22, city = "Mumbai")

 # Function allows code Reusuability

 # Nested Funtions

def outer() :
    def inner() :
        print("I am Inner")
    inner()
    print("I am Outer")

outer()


# Pass By value , Pass By reference
# When we pass an immutable object it's copy gets passed

# strings, integers, float, tuple are immutable objects

# Pass By Reference (mutable objects)
# changes are reflected

def modifyList(list) :
    list.insert(2,4)
    print("Inside Function : ",list)

lst = [1,2,3]

modifyList(lst)

print("Outside Function : ", lst)

