import random
user_wins = 0
comp_wins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_pick = input("Type rock/paper/scissor to play or q to quit: ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        continue
    comp_pick = options[random.randint(0, 2)]
    print("Computer picks", comp_pick, ".")
    if user_pick == "rock" and comp_pick == "scissors":
        print("You win, computer loses")
        user_wins += 1
    elif comp_pick == "rock" and user_pick == "scissors":
        print("You lose, computer wins")
        comp_wins += 1
    elif user_pick == comp_pick:
        print("You win, computer wins" "Its a draw")
        user_wins += 1
        comp_wins += 1
    else:
        print("You lost")
        comp_wins += 1
    print("You won", user_wins,  "," "Computer won", comp_wins)

