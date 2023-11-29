
def read_text_file():
    global words_bank
    file=open("translate.txt","r")
    temp=file.read().split("\n")
    
    words_bank=[]

    for i in range(0,len(temp),2):
        
        my_dic={"en": temp[i] ,"fa":temp[i+1]}
        words_bank.append(my_dic)

    file.close()
def translate_english_to_persian():
    user_text=input("Enter Yor Word :")

    user_words=user_text.split(" ")
    output=""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                output=output+word["fa"]+ " "
                break

        else:
            output=output + user_word + " "  
            
    print(output)  
def show_menu():
    print("Welcome To Translate 💻")
    print("1 - Translate English To persian ")
    print("2 - Translate persian To English")
    print("3 - Add new word to database ")
    print("4 -Exit 👣")

read_text_file()  
while True:
    show_menu()
    choice=int(input("Enter Your Choice : "))
    if choice ==1:
        translate_english_to_persian()

    elif choice ==2:
        ...

    elif choice ==3:
        ...

    elif choice == 4:
        exit(0)