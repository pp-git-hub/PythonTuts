# Lists in Python
# Basically containers for heterogenous datatypes

cars = ["Baleno","Alto","Nano","Creta",234,"Tesla",12.4, "Wagnor", "Swift"]

# indexed (0 based)

print("car at 0th index", cars[0])

# Ordered

# Mutable

cars[0] = "Nano"

print("Car at 0th index : ", cars[0])

# Duplicates allowed

print("Cars at 0th and 2nd index are same : " + cars[0] + " " + cars[2])
# Any DataType

print(cars[4])

# Heterogenous

print(cars)
print(type(cars))
print(len(cars))

if "Nano" in cars :
    print("Nano is there")
else :
    print("Nano absent")

if "BMW" in cars :
    print("BMW is there")
else :
    print("BMW absent")

# -ve indexing means accessing from right side

print(cars[-1])
print(cars[-2])
print(cars[-3])
print(cars[-4])
print(cars[-5])

print(cars[0 : 3])
print(cars[-3 : -1])
print(len(cars))

# append(), insert(), extend()

cars.append("Land Rover")
cars.append("Bolero")

print(cars)

# append() appends at last like push_back() of c++

cars.insert(2,"Skoda")
cars.insert(3,"Seltos")

# insert() inserts at the specified location

cars2 = ["Eon","Fortuner","Ecosport"]

cars.extend(cars2)

print(cars)

# to extend the list by adding a new list we use append

print(cars)

# remove(), pop()

cars.remove("Nano")
# removes a specified element from the begining

print(cars)

cars.pop(3)

# removes an item from the specified index 
# if no index specified then removes from last, like pop_back() in c++

cars.pop()
print(cars)

a = [1,2,3]
b = [1,2,3]

print(a is b)
cars[1:8] = "Lamborghini"
cars[1:8] = "Lamborghini"
print(cars)

# sorting a list 

cars.sort()

print(cars)

# to sort in reverse

cars.sort(reverse = True)

print(cars)

# reverse the list

cars.reverse()

print(cars)

# List Comprehension

age = [12,13,23,24,43,45,20,35]

# to traverse and print a list
for i in age :
    print(i)

# to make a new list out of existing list

newList = [i for i in age if i > 25]

print(newList)

newCars = [car for car in cars if "a" in car]

print(newCars)

new_cars = cars.copy()

print(new_cars)

print(cars is new_cars)

# concatening two lists 

list1 = [1,2,3,4]
list2 = ["Aman","Alok"]

list1 = list2 + list1

print(list1)

# Nested list

list1 = [101,102,103,[104,105]]

# list1[3] = [104,105]

# list1[3][0] = 104

# list1[3][1] = 105

print(list1[3][0])
print(list1[3][1])





