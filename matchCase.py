# making a basic calculator program

num1 = int(input("Please enter 1st number : "))
num2 = int(input("Please enter 2nd number : "))

operator = input("Please enter the operator : ")

match operator :
    case '+':
        print("Sum is ", num1 + num2)
    case '-':
        print("Diff is ", num1 - num2)
    case '*':
        print("Prod is ", num1 * num2)
    case '/':
        print("Quotient is ", num1 / num2)
    case _ :
        print("Please enter a valid Operator")

