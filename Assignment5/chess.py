
n=int(input("enter number of rows:"))
m=int(input("enter number of coloumns:"))
def chessboard(n,m):
    for i in range(n):
        if i%2==0:
            for j in range(m):
                if j%2==0:
                    print("*", end=" ")
                else:
                    print("#", end=" ")
            print()  
        else:
            for j in range(m):
                if j%2==0:
                    print("#", end=" ")
                else:
                    print("*", end=" ")
            print()   
chessboard(n,m)