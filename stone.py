import random

choices = ["stone", "paper", "scissors"]

user_count = 0
computer_count = 0

while user_count >= 10 and computer_count >= 10:
    break

    user = input("Enter stone, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("Draw!")

    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):

        print("You win!")
        user_count += 1

    else:
        print("Computer wins!")
        computer_count += 1

    print("User score:", user_count)
    print("Computer score:", computer_count)
    print("-------------------")

if user_count == 10:
    print("Congratulations! You won the match!")

else:
    print("Computer won the match!")

print("Final score:", user_count, "-", computer_count)