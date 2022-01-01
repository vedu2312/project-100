class Atm:
    def __init__(self,cardno,pin,totalAmount,widdraw):
        self.cardno=cardno
        self.pin=pin
        self.totalAmount=7000
        self.widdraw=widdraw
        
    def cashwiddraw(self):
          print(a1.widdraw)

    def blance(self):
        n=int(a1.totalAmount)-int(a1.widdraw)
        print(n)

          
a1=Atm("c","p","t",300)
print(a1.cardno)
print(a1.pin)        
a1.cashwiddraw()
a1.blance()