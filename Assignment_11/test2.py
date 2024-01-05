class Fraction:

    def __init__ (self,ss,mm):

        self.s=ss
        self.m=mm


    def sum(self,k1):

        res_s=k1.s*self.m + k1.m*self.s
        res_m=k1.m * self.m

        x=Fraction(res_s,res_m)
        return x
        

    def mul(self,k2):

        res_s=self.s * k2.s
        res_m=self.m * k2.m
        
        x=Fraction(res_s,res_m)

        return x
    
    def div(self):
        ...


    def fraction_to_number(self):
        ...



    def show(self):
        print(self.s, "/",self.m)



print("Fraction One : ")
a=Fraction(10,12)
a.show()

print("Fraction two : ")

b=Fraction(3,7)
b.show()

print("Fraction Mul : ")

z=a.mul(b)

z.show()                       
print("Fraction Sum : ")

f=b.sum(a)
f.show()