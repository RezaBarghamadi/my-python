from manage_media import Media
from film import Film
from clip import  Clip
Media=[]
def show_menu():
    print("This is  Menu 👀")
    print("1-Add Media")
    print("2-Edited Media")
    print("3-deleted Media")
    print("4-search Media")
    print("5-show Media")
    print("6-exit")

def add_media():
    print("For Add Film Enter : 1")
    print("For Add Clip Enter : 2")
    print("For Add Documentary Enter : 3")
    print("For Add Series  Enter : 4")

    user=int(input("Please Enter Your Choise:"))
    
    if user==1:
        type = "Film"
        name = input("Enter name: ")
        directory = input("Enter directory: ")
        imdb = input("Enter IMDB score: ")
        url = input("Enter download link: ")
        year = input("Enter year: ")
        casts = input("Enter casts: ")
        Media.append(Film(type, name, directory, imdb, url, year, casts))

    elif user==2:
        type = "Series"
        name = input("Enter name: ")
        directory = input("Enter directory: ")
        imdb = input("Enter IMDB score: ")
        url = input("Enter download link: ")
        year = input("Enter year: ")
        casts = input("Enter casts: ")
        Media.append(Film(type, name, directory, imdb, url, year, casts))


    
    elif user==3:
        ...

    elif user==4:
        ... 


print("Data Loading ...")
while True:
    show_menu()
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        add_media()
    elif choice==2:
     ...
    elif choice== 3:
        ...
    elif choice==4:
        ...
    elif choice==5:
            ...
            break
    elif choice==6:
         exit(0)
    else:
        print("Please Enter Num Just This Menu!!!!!!!")  