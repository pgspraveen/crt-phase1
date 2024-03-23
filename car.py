class carshowroom:
    def _init_(self):
        cgst=2000
        sgst=1000
        insurence=45000
        amount=cgst+sgst+insurence
        self.amount=amount
    def company(self,company_name):
        company_name=input('enter the name')
        print('wellcome to ',company_name,'family')
        self.company_name=company_name
        
    def model(self,model):
        if self.company_name=='mahendra':
            l1=['thar','xuv700']
            print(l1)
        elif self.company_name=='volkswagen':
            l2=['virtus','taigun']
            print(l2)
        elif self.company_name=='toyota':
            l3=['vellfire','fortuner']
            print(l3)
        else:
            print('not found')
            carshowroom()            
        modelname=input('enter the model')
        self.model=model
        print(self.model)
    def price(self):
        if self.model=='thar':
            exshowroom=1410000
            print('x-showroom price:1410000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='xuv700':
            exshowroom=2699000
            print('x-showroom price:2699000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='virtus':
            exshowroom=1941000
            print('x-showroom price:1941000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='taigun':
            exshowroom=1170000
            print('x-showroom price:1170000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='vellfire':
            exshowroom=13000000
            print('x-showroom price:13000000')
            print('onroad price:',exshowroom+self.amount)
        elif self.model=='fortuner':
            exshowroom=5144000
            print('x-showroom price:5144000')
            print('onroad price:',exshowroom+self.amount)
        else:
            print('not found')
            carshowroom()
            
obj=carshowroom()
obj.company('mahendra')
obj.model('thar')
obj.price()
