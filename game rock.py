import random

rock_ascii="🪨"

paper_ascii="🫱"

scissors_ascii="✄"

print("welcome to the Rock, Papeer, Scissors  \n")
comnfirm=input("press enter to continue or type (Help) for the rules. \n").lower()


if comnfirm == "help":
    print("""
    ******Rules******"
    1)you choose and the computer chooses"
    2)Rock smashes Scessors -> Rock win"
    3)Scissors cut Paper -> Scissors win"
    4)Paper covers Rock -> Paper win""")
   
    
user_choice=input("Enter your choice (Rock, Paper, Scissors) :").lower()

if user_choice not in ["rock", "paper","scissors"]:
    print("Invalid choice. Please Run the program again and choose rock, paper, or scissors.")

else:
    if user_choice == "rock":
        print(f"\nyou chose: {rock_ascii}")

    elif user_choice == "paper":
        print(f"\nyou chose: {paper_ascii}")

    else:
        print(f"\nyou chose: {scissors_ascii}")



computer_choice=random.choice(["rock","paper","scissors"])

if computer_choice == "rock":
    print(f"computer chose:{rock_ascii}")


elif computer_choice == "paper":
    print(f"computer chose:{paper_ascii}")


else:
    print(f"computer chose:{scissors_ascii}")



    if user_choice==computer_choice:
        print("It's a tie.")

    elif (
        (user_choice== "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
    
        print(f"you win! {user_choice} beats {computer_choice}")

    else:
        print(f"you lose! {computer_choice} beats {user_choice}")