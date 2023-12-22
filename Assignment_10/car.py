class my_car:
    def __init__(self,c,co,max):
        self.color=c
        self.company=co
        self.max_speed=max


    def drive(self):
        print("GHAN GHAN")

    def start(self):
        ...



car1=my_car("red","BMW",320)
car2=my_car("with","BENZ",300)
car3=my_car("orange","Freary",400)

print(car3.max_speed)

car3.drive()