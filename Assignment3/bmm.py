x=int(input("Emter X :"))
y=int(input("Emter Y :"))
n=z=0
if x>y:
    n=x
else :
    n=y
for i in range(1,n+1):
    if x%i==0 and y%i==0:
        z=i
        print("adad bakhesh pazir :",z)

print(z)

          