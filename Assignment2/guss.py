import random
print ("Enter one Number For Start This Game")
computer_number= random.randint(1,10)
while 1==1:
    person_number=int(input())

    if computer_number==person_number:
        print("Sucsses 😍")
        break
    elif computer_number< person_number:
        print("kamesh kon 📥")
    elif computer_number > person_number:
        print("bishtaresh kon 📤")

