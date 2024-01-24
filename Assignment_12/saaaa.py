import time
import pyfiglet
from media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actors import Actors


print(
    "                                                    Loading")
time.sleep(1)
three = pyfiglet.figlet_format("3")
print(three)
time.sleep(1)
tow = pyfiglet.figlet_format("2")
print(tow)
time.sleep(1)
one = pyfiglet.figlet_format("1")
print(one)
time.sleep(1)

# movie = Media("man of steel", "zack snyder", "7.1",
#               "https://youtu.be/EVsFbdjlpAE", "2013", "henry cavill")
# movie.showinfo()
# movie.download()
media = []


def read_data():
    f = open("episode12/database.txt", "r")
    file_read = f.read()

    media = file_read.split("\n")
    for i in range(len(media)):
        split = media[i].split(",")
        if split[0] == "film":
            media.append(
                Film(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))
        elif split[1] == "series":
            media.append(Series(
                split[0], split[1], split[2], split[3], split[4], split[5], split[6]))
        elif split[2] == "documentary":
            media.append(Documentary(
                split[0], split[1], split[2], split[3], split[4], split[5], split[6]))
        elif split[3] == "clip":
            media.append(
                Clip(split[0], split[1], split[2], split[3], split[4], split[5], split[6]))
        return media

    f.close()


media = read_data()
# print(media)


def show_menu():
    print("1.Add Media\n2.Search\n3.Edit\n4.Remove\nDownload")


def add_media():
    print("1.Film\n2.Series\n3.Documentary4.Clip")
    user_input = int(input("Enter your choice"))

    if user_input == 1:
        type = "Film"
        name = input("Enter name: ")
        directory = input("Enter directory: ")
        imdb = input("Enter IMDB score: ")
        url = input("Enter download link: ")
        year = input("Enter year: ")
        casts = input("Enter casts: ")
        media.append(Film(type, name, directory, imdb, url, year, casts))

    elif user_input == 2:
        type = "Series"
        name = input("Enter name: ")
        directory = input("Enter directory: ")
        imdb = input("Enter IMDB score: ")
        url = input("Enter download link: ")
        year = input("Enter year: ")
        casts = input("Enter casts: ")
        session = input("Enter session's number: ")
        media.append(Series(type, name, directory,
                     imdb, url, year, casts, session))

    elif user_input == 3:
        type = "Documentary"
        name = input("Enter name: ")
        directory = input("Enter directory: ")
        imdb = input("Enter IMDB score: ")
        url = input("Enter download link: ")
        year = input("Enter year: ")
        casts = "None"
        media.append(Documentary(
            type, name, directory, imdb, url, year, casts))

    elif user_input == 4:
        type = "Clip"
        name = input("Enter name: ")
        directory = input("Enter directory: ")
        imdb = input("Enter IMDB score: ")
        url = input("Enter download link: ")
        year = input("Enter year: ")
        casts = input("Enter casts: ")
        media.append(Clip(type, name, directory, imdb, url, year, casts))

# work later


def search():
    user_input = input("Please Enter name of media: ")
    for media in media:
        if user_input == media.name:
            media.show_info()


def edit():
    user_input = input("Enter name of media: ")
    for media in media:
        if user_input == media.name:
            name = input("Enter Name: ")
            director = input("Enter Director: ")
            iMDBScore = int(input("Enter IMDBScore: "))
            url = input("Enter Url: ")
            year = input("Enter Year: ")
            casts = input("Enter Casts: ")
            res = [name, director, iMDBScore, url, year, casts]
            media.append(res)

    else:
        print("No exist")


def remove():
    user_input = input("Enter Name Media: ")
    for media in media:
        if user_input == media.name:
            media.remove(media)
    else:
        print("No exist")


def download():
    user_input = input("Enter Name Media: ")
    for media in media:
        if user_input == media.name:
            Media.download(media)

    else:
        print("No exist")


while True:
    show_menu()
    choice = int(input("Enter Choice: "))
    if choice == 1:
        add_media()
    elif choice == 2:
        search()
    elif choice == 3:
        edit()
    elif choice == 4:
        remove()
    elif choice == 5:
        download()