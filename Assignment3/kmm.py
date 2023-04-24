x=int(input("Emter X :"))
y=int(input("Emter Y :"))
n=z=0
j=(x*y) +1

if x>y:
    n=x
else :
    n=y

for i in range(n,j ):
    if i%x ==0 and i%y==0:
       z=i     
       
print(z)