import random

print("\nWelcome to my Harry Potter Number Guessing Game!")
print("Get ready to test your magical powers! 🧙✨🔮\n")

def play_game():
    top_of_range = input("Enter the highest number for your magical range: ")

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
        user_guess = input("Cast your guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time.")
            continue
        
        if user_guess == random_number:
            print("\nYou got it! 🎉 Guessus correctus!\n")
            break
        elif user_guess > random_number:
            print("Your guess soared higher than The Golden Snitch! ʚ🟡ɞ Try a lower guess!")
        else:
            print("Your guess sank lower than merpoeple in The Black Lake! 🧜‍ Try a higher guess!")
    
    if guesses > round(top_of_range * 0.2):
        print("But... Not very psychic of you. You cast the right spell in", guesses, "guesses... Witchery might not be your strength.")
    else:
        print("Wow, you might have the true magical powers! 🧙✨ You cast the right spell in", guesses, "guesses...")


while True:
    play_game()
    play_again = input("Do you dare to play again? (yes/no): ")
    if play_again.lower() != "yes":
        print("Thanks for testing your magic!")
        break