
# Recursion : It is a Process where "a function is Calling itself"

# Factorial using Recursion

num = 5

def fact(num) :
    if(num == 0) : 
        return 1
    return num * fact(num -1)

print(fact(num))

