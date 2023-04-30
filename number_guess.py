import random

print("Welcome to my Harry Potter Number Guessing Game!")
print("Get ready to test your powers! 🔮")

def play_game():
    top_of_range = input("Type a number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please type a number larger than 0 next time.")
            quit()
    else:
        print("Please type a number next time.")
        quit()


    random_number = random.randint(0, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = input("Guess a number: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time.")
            continue
        
        if user_guess == random_number:
            print("You got it!")
            break
        elif user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")

    print("You got it in", guesses, "guesses.")
    if guesses > 2:
        print("Not very psycic of you...")
    else:
        print("Wow, you might have the powers!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for playing! :)")
        break