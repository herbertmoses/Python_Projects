from random import randint

guess = 0
secret_number = randint(1, 100)
estimation = 0
name = input("Tell me your name: ")

print(f"Ok {name}, I have thought of a number between 1 and 100\nYou have 8 guesses to guess")

while guess < 8:
    estimation = int(input("What is the number?: "))
    guess += 1

    if estimation < secret_number:
        print("My number is higher")
    elif estimation > secret_number:
        print("My number is lower")
    else:
        print(f"Congratulation {name}! You have guessed in {guess} attempts")
        break

if estimation != secret_number:
    print(f"Sorry, we have run out of attempts. The secret number was {secret_number}")

