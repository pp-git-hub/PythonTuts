

# Factorial using function

def fact(num) :
    if(num < 0) :
        return "NAN"
    fact = 1
    for i in range(1,num + 1) :
        fact *= i
    return fact

num = int(input("Please enter a number : "))

print("Factorial of ", num, " is ", fact(num))