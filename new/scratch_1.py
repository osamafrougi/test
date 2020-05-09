class Accouunt:
    def __init__(self,name,balnce,mainblance):
        self.name=name
        self.balnce=balnce
        self.mainblance=mainblance

    def diposit(self,amount):
        self.balnce += amount

    def withrow(self,amount):

       if self.balnce-amount>=self.mainblance:

          self.balnce-=amount
       else:
        print("balnce is not enough")