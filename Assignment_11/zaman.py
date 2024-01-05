class Time:
    def __init__ (self,h,m,s):

        self.h=h
        self.m=m
        self.s=s
        self.fix_time()


    def show(self):

        print(self.h,":",self.m,":",self.s,":")
    

    def sum_time(self,other):
        
        new_h=self.h + other.h
        new_m=self.m+ other.m
        new_s=self.s + other.s
        t=Time(new_h,new_m,new_s)
        return t


    def sub_time(self,other):

        new_h=self.h - other.h
        new_m=self.m -  other.m
        new_s=self.s - other.s
        
        t=Time(new_h,new_m,new_s)
        return t
    

    def fix_time(self):
        if self.s >= 60:
            self.s -= 60
            self.m +=1 

        if self.m >= 60:
            self.m -= 60
            self.h += 1

        if self.s < 0:
            self.s +=60
            self.m -=1

        if self.m <0 :
            self.m +=60
            self.h -=1
       
       


t1=time=Time(17,40,33)
t1.show() 

t2=time=Time(2,30,55)
t2.show() 

sum= t1.sum_time(t2)
sum.fix_time()
