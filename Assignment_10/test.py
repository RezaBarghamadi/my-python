class person:
    def __init__(self,a,c,m,city):
        self.age=a
        self.countery=c
        self.majer=m    
        self.city=city
        self.spouse=None


    def eat(self):
        ...
    def sleep(self):
        ...       
    def marred(self,name):
        self.spouse=name



my_frend=person(21,"IRAN","AI","Sabzevar")
print(my_frend.spouse)

my_frend.marred("Maryam")
print(my_frend.spouse)
