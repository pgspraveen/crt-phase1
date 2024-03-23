#write a program to accept the ticket price of a movie from user if the price false/lies between 250 and 300 print recliners if the ticket price b/w 150 and 200 print gold. if the ticket price b/w 100 and 150 silver if the tkt price b/w 200 and 250 print platinum
#otherwise print balcony
tkt = int(input("value of price "))
if tkt>250 and tkt>=300:
    print("recliners")
elif tkt>150 and tkt>=200:
    print("gold")

elif tkt>100 and tkt>=150:
    print("silver")
    
elif tkt>200 and tkt>=250:
    print("platinum")
else:
    print("balcony")



