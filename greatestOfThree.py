
a = int(input("Please enter 1st number : "))
b = int(input("Please enter 1st number : "))
c = int(input("Please enter 1st number : "))

if a < b :
    if b > c :
        print(b, " is the greatest number")
    else :
        print(c, " is the greatest number")

elif a > c :
    print(a, " is the greatest number")

else :
    print(c, " is the greatest number")
