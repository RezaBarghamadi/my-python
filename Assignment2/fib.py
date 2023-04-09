print ("Enter One Number To show Fib : ")

while True:
    num=int(input())
    f=[1]
    if num==1:
        print(f)
        
    elif num==2:
        f.append(1)
        print(f)
        
    elif num>2:
        f.append(1)
        for i in range(2,num):
            fi=f[i-1]+f[i-2]
            f.append(fi)
        
        print(f)