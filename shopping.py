class shopping:
    def __init__(self,place):
        self.place=place
        print("welcome to shopping",place)
    def dresstype(self,mat):
        print("dresstype is:",mat)
        self.m=mat
    def price(self,value):
        print("price is:",value)
        self.v=value
    def size(self,sz):
        print("size is:",sz)
        self.s=sz
    def display(self):
        print("material",self.m)
        print("price",self.v)
        print("size",self.s)
        print("bye bye",self.place)
total=shopping("trends")
total.dresstype("cotton")
total.price(5000)
total.size("l")
total.display()





















    
