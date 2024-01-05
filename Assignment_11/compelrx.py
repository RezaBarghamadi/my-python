class Complex:
    def __init__(self,real,image):

        self.real=real
        self.image=image

    def com_sum(self,com):
        real=self.real + com.real
        image=self.image+com.image

        r=Complex(real,image)

        return r

    def com_sub(self,com):
        real=self.real - com.real
        image=self.image- com.image

        r=Complex(real,image)
        return r
    
    def com_mul(self,com):

        real=self.real * com.real - self.image* com.image

        image=self.real * com.image +self.image *com.image
        r=Complex(real,image)
        return r


    def com_show(self):

        print(self.real , "+" , "i" , self.image)



a=12
b=25

c=42
g=27
print("My Compelex Number ")
x=Complex(a,b)
x.com_show()

y=Complex(c,g)
y.com_show()
print("Add My Complex Number :")

r=x.com_sum(y)
r.com_show()

print("ُSub My Complex Number :")

r=x.com_sub(y)
r.com_show()


print("Mol My Complex Number :")

r=x.com_sub(y)
r.com_show()