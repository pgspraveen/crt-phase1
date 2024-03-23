dict={104:"a",103:"b",105:"c","104":"e"}
dict[104]="e"
print(dict)
for i in dict:
    print(i)
for x in dict.values():
    print(x)
for x,y in dict.items():
    print(x,y)
dict.pop("104")
print(dict)
