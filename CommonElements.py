
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)

s4 = s1.intersection(s2)
s4 = s4.intersection(s3)

print(s4)
