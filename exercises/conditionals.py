# Write your solution for 1.2 here!
import math
b=0
for i in range(100):
    if i%2==0:
        b+=i
print(b)

c=0
max=0
for i in range(1000):
    if i%6==2 and math.pow(i,3)%5==3 and i>max:
        max=i
print(max)