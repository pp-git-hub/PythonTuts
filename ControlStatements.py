# if, if-else, nested if, else if ladder, ternary,switch 
# if - else

isRaining = True

if isRaining :
    print("Keep Umbrella")
else :
    print("Don't Keep Umbrella")

age = 14

if age < 18 :
    print("Can't vote")

else :
    print("Please Vote")


temp = 17

if temp > 45 :
    print("It's too hot outside")

elif temp <= 22 and temp >= 18 :
    print("It's bit cold outside")

elif temp < 18 and temp > 10 :
    print("It's cold outside")

else :
    print("It's very cold outside")
