import random

def guess_number_and_win():
    rand_value = random.randint(1, 100)
    print("You have 5 chances to guess the number.")
    print("1st chance: 5X the entered amount\n2nd chance: 3X the entered amount\n3rd chance: 2X the entered amount\n4th chance: 1.5X the entered amount\n5th chance: 1X the entered amount")

    price_value = int(input("Enter the amount you want to bet in rupees: "))
    rewards = [5 * price_value, 3 * price_value, 2 * price_value, 1.5 * price_value, 1 * price_value]

    for i in range(1, 6):
        print(f"\nAttempt {i}:")
        guess_value = int(input("Guess a number between 1 and 100: "))
        
        if 1 <= guess_value <= 100:
            if guess_value == rand_value:
                print("Congratulations! You guessed the correct number.")
                print(f"You won: {rewards[i-1]} rupees.")
                break
            else:
                hint = check_user_input(guess_value, rand_value)
                print(hint)
        else:
            print("You entered an invalid number. Please guess a number between 1 and 100.")

    else:
        print(f"Sorry, your 5 chances are over. The correct number was {rand_value}. Better luck next time!")

def check_user_input(guess_value, rand_value):
    if guess_value > rand_value:
        return "Too high! Try a smaller number."
    else:
        return "Too low! Try a larger number."


guess_number_and_win()

