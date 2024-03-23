#accept 3 subject marks from user if the student has score above 80 in all the three subjects then print A+.if the student has score above 60&below 80  in all the subject print B otherwise pass

a = int(input("python marks"))
b = int(input("java marks"))
c = int(input("c mARKS"))

if a<=80 and b<=80 and C<=80:
        print("A+")
elif  a>60 and a<80 and b>60 and b<80 and c>60 and c<80:
    print("B")
else:
    print("pass")
