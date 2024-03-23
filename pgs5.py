#accept a number from user and check if it is divisible by 3 and 5 print great.if the number is divisible by 3 and 9 if it is divisible by 3 and 7 print ok otherwise not ok
a = int(input("value of a"))
if a//3 and a//5:
    print("great")
elif a//3 and a//9:
    print("good")

elif a//3 and a//7:
    print("ok")
else:
    print("notok")

