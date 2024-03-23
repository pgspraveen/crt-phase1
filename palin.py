n=153
sum=0
i=3
while n>0:
    a=n%10
    sum=(sum+a)
    d=sum**i
    n=n//10
print(sum)
if n%sum==0:
    print("s")
else:
    print("no")
    
