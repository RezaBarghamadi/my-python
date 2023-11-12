import pyfiglet
from termcolor import colored

def color():
    Pel1=" X "
    pel2=" O"

    colored(Pel1, "red")
    colored(pel2, "blue")

def show():
    for row in game_chart:
        for cell in row :
            print(cell ,end=" ")
        print()   
        
def check_player():
    if game_chart[0][0]=="X" and game_chart[0][1]=="X" and game_chart[0][2]=="X":
     print("Player 1 id Win 😍")

    if game_chart[1][0]=="X" and game_chart[1][1]=="X" and game_chart[1][2]=="X":
     print("Player 1 id Win 😍")

    if game_chart[2][0]=="X" and game_chart[2][1]=="X" and game_chart[2][2]=="X":
     print("Player 1 id Win 😍")




title= pyfiglet.figlet_format("Tic Tak Toe",font="slant")
print(colored(title, "yellow"), end='')


game_chart=[["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]]

while True:
    print(colored("Player 1 : X","red"))     
    while True:
        row=int(input("Enter Num row: ")) 
        col=int(input("Enter Num colem :"))
        if  0<= row <=2 and  0<=col <=2 : 
            if game_chart[row][col]== "-":
                game_chart[row][col] = colored("X","red")
                
                break
            else:
                print("Ghablan Entekhab Shodeh 😥 ")
        else:
            print("Plese Enter  0 && 1 && 2")        
    show()
    check_player()
    print(colored("player 2  O :","blue"))
    while True:
        row=int(input("Enter Num row: "))
        col=int(input("Enter Num colem :"))
        if  0<= row <=2 and  0<=col <=2 :
            if game_chart[row][col]== "-":
                game_chart[row][col] = colored("O","blue")
                break
            else:
                print("Ghablan Entekhab Shodeh 😥 ")
        else:
            print("Plese Enter  0 && 1 && 2")
    show()
    check_player()