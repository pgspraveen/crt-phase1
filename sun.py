n=2156
s=0
n1=n
while n>0:
    d=n%10
    s=s+d
    n=n//10
print(s)
if n1%s==0:
    print("divisible")
else:
    print("not")
