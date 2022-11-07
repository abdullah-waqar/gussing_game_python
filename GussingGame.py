import random

print("Welcome to the gussing game!")

randomNumber = random.randint(1 , 5)

user_guess = None

guesses = 0

while(user_guess != randomNumber):
    user_guess = int(input("Enter your guess: "))
    guesses += 1
    if(user_guess == randomNumber):
        print(f"You guessed it right in {guesses} guesses")
        with open("userScore.txt" , "r") as f:
            data = f.read()
        if(data == ''):
            with open("userScore.txt" , "w") as f:
                f.write(str(guesses))
                print("New high score")
        else:
            with open("userScore.txt" , "w") as f:
                if (guesses < int(data)) :
                    print("New high score")
                    f.write(str(guesses))

    else:
        if(user_guess > randomNumber):
            print("You guessed it wrong. Enter a smaller number")
        else:
            print("You guessed it wrong. Enter a larger number")

