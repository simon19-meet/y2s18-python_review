# Write your solution for 1.3 here!
a=1
sum=0

while sum<10000:
    sum+=a
    a+=1
print(a)
print(sum)

b=0
sum2=0
while sum2<10000:
    if b%2==0:
        sum2+=b
    b+=1
print(b)
print(sum2)
