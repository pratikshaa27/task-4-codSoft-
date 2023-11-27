import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

# Define the rules
rules = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

num_rounds = int(input("How many times do you want to play? "))

for i in range(num_rounds):
    user_choice = input("Choose rock, paper, or scissors: ")
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif rules[user_choice] == computer_choice:
        print("You win!")
        user_score += 1
    else:
        print("The computer wins!")
        computer_score += 1

print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")

if(computer_score>user_score):
    print("Computer win the Game!!")
elif(user_score>computer_score):
    print("You win the Game!!")
else:
    print("its a tie........")
