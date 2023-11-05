print("Enter Number for  print  one diamod for you 🥰 :")
a=int(input())
def display_diamond(n):
    for i in range(n):
        print(' '*(n-i-1) + '* '*(i+1) )
    for i in range(n):
        print(' '*(i+1) + '* '*(n-i-1))

display_diamond(a)