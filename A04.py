import random


choices = ["rock", "paper", "scissors"]


computer_choice = random.choice(choices)


user_choice = input("Choose rock, paper, or scissors: ").lower()


print(f"The computer chose {computer_choice}.")


if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
else:
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
