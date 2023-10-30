# Mirroring here means a -> z, b -> y and so on...

# for eg: Input  : paradox , Output : 

word = input("\nPlease Enter a Word : ")

result = ""

for i in range(0, len(word)) :
    result += chr((122 - ord(word[i]) + ord('a')))

print(result)

# Another smart way of doing above task is 

alphabets = "abcdefghijklmnopqrstuvwxyz"

reverse = alphabets[ : : -1] # -1 represents right to left moving by 1 step

# using Zip function

dict1 = dict(zip(alphabets,reverse)) # performs zipping then a dictionary

print(dict1)

res = ""

for i in word :
    res += dict1[i]

print(res)

