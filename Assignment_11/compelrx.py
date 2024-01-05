class Complex:
    def __init__(self,real,image):

        self.real=real
        self.image=image

    def com_sum(self):
        ...

    def com_sub(self):
             ...

    def com_show(self):

        print(self.real , "+" , "i" , self.image)



a=12
b=25

x=Complex(a,b)
x.com_show()

