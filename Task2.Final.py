from random import randint

def GuessNumber():
    number = int(randint(0,100))
    while True: 
        UserInt = int(input("Guess a number between 0-100. \n"))

        if UserInt == number:
            print(f"{number} is correct!")
            break
        elif number < UserInt:
            print("Lower")
        else:
            print("Higher")

GuessNumber()