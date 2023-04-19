import random

word_banck=["blue","red","mouse","mobile","water","book","pen","paper","lamp","fly","wier","room"]
user_mistaks=0
false_guess=[]
true_guess=[]
x=random.randint(0,len(word_banck)-1)

while user_mistaks <6:
    word=word_banck[x]
    for i in range(len(word)):
        if word[i] in true_guess:
             print (word[i] ,end=" ")
        else:
            print(" - " ,end=" ")
    if true_guess== word[i]:
        print (" Good You have Win 😍👌")
        break
    user_guess=input("plese Enter Your Word guess :")    
    user_guess = user_guess.lower()
    if len(user_guess)==1:
        if user_guess in word:
            true_guess.append(user_guess)
            print( " Thats Right 😍 ")

        else:
            false_guess.append(user_guess)
            user_mistaks =user_mistaks + 1 
            print ( "User Mistakes : ",user_mistaks)
            print("Oh No 😭")
    else:
        print (" ☹ You can only enter one character:")
if user_mistaks ==6:
    print("Oh Yoy Game Over ☠☠☠")