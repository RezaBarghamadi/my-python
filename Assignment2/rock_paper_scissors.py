import random

print ("Hi Welcome to this Game ")
user_score=0
computer_score=0

x=random.randint(1,3)
for i in range(3):
    if x==1 :
        computer_choice="sang"
    elif x==2:
        computer_choice="kaghaz"
    elif x==3:
        computer_choice="ghychi"

        user_choice=input()



        if computer_choice=="sang" and user_choice=="kaghaz ":
            user_choice=user_score + 1
        # elif computer_choice=="ghychi" and user_choice=="sang" :
        #     user_choice=user_choice + 1
        # elif computer_choice=="kaghaz" and user_choice=="sang" :
        #     computer_choice=computer_score + 1
        # elif computer_choice=="kaghaz" and user_choice=="kaghaz" :
        #      computer_choice=computer_score +0
        # elif computer_choice=="ghychi" and user_choice=="ghychi" :
        #     user_choice=user_score +0
        # elif computer_choice=="sang" and user_choice=="sang" :
        #     computer_choice=computer_score +0
        # elif computer_choice=="kaghaz" and user_choice=="ghychi" :
        #     user_choice=user_score +1
        # elif computer_choice=="ghychi" and user_choice=="kaghaz" :
        #     computer_choice=computer_score + 1
        # elif computer_choice=="kaghaz" and user_choice=="sang" :
        #     computer_choice=computer_score + 1
        print("💻",computer_choice)
        print("👨",user_choice)

        print("user_score :" ,user_score ) 
        print("computer_score : " ,computer_score )