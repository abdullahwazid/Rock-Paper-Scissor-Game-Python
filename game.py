import random #Library for random choices for the computer

options = ["ROCK", "PAPER", "SCISSORS"];

while True : #Outer Loop for Replay

    while True : #Inner Loop for checking valid Input
        player = input("Enter Your Choice(Rock, Paper or Scissors) : ").upper()
    
        if player not in options : 
            print("Invalid Choice! Please Try Again.\n")
            continue 

        break

    computer = random.choice(options)
    print("You Chose : ", player)
    print("Computer Chose : ", computer)

    if player == computer : 
        print("Match Tied!")
    elif(player == "ROCK" and computer == "SCISSORS") or \
    (player == "PAPER" and computer == "ROCK") or \
    (player == "SCISSORS" and computer == "PAPER") : 
        print("You Won!")
    else : 
        print("Computer Won!")

#replay 

    replay = input("Play Again? (Y/N) : ").upper();
    if replay == "Y" : 
        continue
    elif replay == "N" : 
        print("Thank You! Game Exited.")
        break
    else : 
        print("Invalid Choice! Exiting the Game.")
        break