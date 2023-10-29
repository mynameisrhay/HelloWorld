# 5th exercise. in this guessing game, there's a secret number that a user can guess for 3 times. need to exercise
# while loop for this program.

secret_number = "9"
tries = 0

while tries < 3:
    guess = input("Guess: ")
    tries += 1
    if guess == secret_number:
        print("You guessed it right!")
        break
    elif tries >= 3:
        print("3 tries done!")
