import random

computer_number= random.randint(1,10)
for i in range(10):
    person_number=int(input())

    if computer_number==person_number:
        print("Sucsses 😍")
        break
    elif computer_number< person_number:
        print("kamesh kon 📥")
    elif computer_number > person_number:
        print("bishtaresh kon 📤")

