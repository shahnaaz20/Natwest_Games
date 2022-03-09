import random

def Game():
    
    def win():
        print("you win!")

    def lose():
        print("you loss!")

    computer_score = 0
    player_score = 0 
    while True:
        player_choice=input("what do you pick? \nRock Paper Scissor : ")
        player_choice.strip()
        random_moves=random.randint(0,2)
        moves=["rock","paper","scissor"]
        computer_choice=moves[random_moves]

        print(computer_choice)

        if player_choice==computer_choice:
            print("Is a tie play again")

        elif player_choice=="rock" and computer_choice=="scissor":
            player_score+=1
            win()
        elif player_choice="rock" and computer_choice="paper":
            computer_score+=1
            lose()
        elif player_choice=="paper" and computer_choice=="scissor":
            computer_score+=1
            lose()
        elif player_choice=="scissor" and computer_choice=="paper":
            player_score+=1
            win()
        elif player_choice=="scissor" and computer_choice=="rock":
            computer_score+=1
            lose()
        elif player_choice=="paper" and computer_choice=="rock":
            player_score+=1
            win()
        elif player_choice not in moves:
            print("Invalid Input")

        again=input("do you want to play again? [y/n] : ").strip().lower()

        if again=="n":
            print("player_score - ",player_score,"computer_score - ",computer_score)
            print("Thank you for playing")
            break

Game()