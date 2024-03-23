def isprime():
    f=1
    n=int(input("enter the number"))
    for i in range(2,n):
        if n%i==0:
            f=0
            break
    if f==1:
        print("prime")
    else:
        print("not prime")
isprime()
