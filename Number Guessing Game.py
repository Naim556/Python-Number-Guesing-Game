import random

def user_get_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).strip()
        if valid_options:
            if user_input.capitalize() in valid_options:
                return user_input.capitalize()
            else:
                print(f"Invalid input. Please choose one of {valid_options}.")
        else:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")


def play():
    print("\nStarting the game! Try to guess the number.\n")
    keep_playing = True
    while keep_playing:
        select_number = user_get_input("Please select a number between 1 and 6: ")

        rand_number = random.randrange(1, 7)
        if  1 <= select_number <= 6:
            if select_number == rand_number:
                print(f"User: {select_number} and Random Number: {rand_number}\nyou won :)")
            else:
                print(f"User: {select_number} and Random Number: {rand_number}\nyou lose :(")

            continue_ = input("If you want to continue[Y|N]: ")

            if continue_.capitalize() == "Y":
                print("so continue game.")
                
            elif continue_.capitalize() == "N":
                print("Thank you for play games, good bye.")
                break
            else:
                print("I don't understand what you mean, that's why I'm leaving.")
                break
        else:
            print("Please enter number between 1, 6.")

def main():
    print("Hello, this is a number guessing game.\n")

    start_game = user_get_input("Do you want to play? [Y/N]: ", valid_options=["Y", "N"])

    if start_game == "Y":
        play()
    elif start_game == "N":
        print("Thanks for visiting and running the code.")
    else:
        print("I don't understand what you mean, that's why I'm leaving.")



if __name__ == "__main__":
    main()