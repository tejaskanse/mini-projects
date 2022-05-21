import random

rock = '''
    _______
---'    _____)
         (______)
         (_______)
         (______)
---.__(____)
'''

paper = '''
    ______
---'   ____)___
          ________)
          __________)
         _________)
---.________)
'''

scissors = '''
    ______
---'   ____)____
          ________)
       __________)
       (____)
---.(____)
'''
game_images=[rock,paper,scissors]
while(True):
    user_choice=int(input("what do you choose? type 0 for rock, 1 for paper, 2 for scissors.\n"))
    if user_choice>=3 or user_choice<0:
        print("you typed an invalid number, game over!")
        break
    else:
        print(game_images[user_choice])
        
        comp_choice= random.randint(0,2)
        print(f"computer chose {comp_choice}")
        print(game_images[comp_choice])

        if user_choice==0 and comp_choice==2:
            print("you win!")
        elif comp_choice==0 and user_choice==2:
            print("you lose!")
        elif comp_choice > user_choice:
            print("you lose!")
        elif user_choice>comp_choice:
            print("you win!")
        elif user_choice==comp_choice:
            print("it's a draw")











    
