
for _ in range(10) :
    print("A" * 5)

for _ in range(6) :
    for i in range(1,7) :
        print(i, end = "") 
    print()

for i in range(1,5) :
    for j in range(1,i + 1) :
        print(j, end = "")
    print() 

for i in range(65,69) :
    for j in range(65,i + 1) :
        print(chr(j), end = "")
    print() 

"""
     1
    1 2 3
  1 2 3 4 5
1 2 3 4 5 6 7

"""
n = int(input("Please enter the number of rows : "))

for i in range(1,n + 1) :
    # for spaces
    print(" " * (n - i), end = "")
    
    # for numbers
    for j in range(1, 2 * i) :
        print(j, end = "")
    print() 

