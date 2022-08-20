import secrets


def random_number_by_pc():
    """This function returns a random number below a certain integer. 100 in this implementation."""
    print("PC has picked a whole number between 0 and 100.\nCan you guess it?")
    return secrets.randbelow(100)


def game_loop(level_diff, number):
    """This function is the main gameloop function. It gets the difficulty and the number to guess as inputs.
    Ends when the number of attempts reaches the number allowed by the difficulty level or if the player guesses the number."""
    global number_of_guesses
    guessed_number = -1
    if level_diff == 1:
        number_of_guesses = 4
        print("You have 4 attempts to get the number right")
        while guessed_number != number  and number_of_guesses != 0:
            get_guess = int(input("What is your guess? "))
            guessed_number = get_guess
            if guessed_number != number:
                number_of_guesses -= 1
                if number < guessed_number:
                    print("You guessed higher!")
                else:
                    print("You guessed lower!")
    elif level_diff == 2:
        number_of_guesses = 6
        print("You have 6 attempts to get the number right")
        while guessed_number != number  and number_of_guesses != 0:
            get_guess = int(input("What is your guess? "))
            guessed_number = get_guess
            if guessed_number != number:
                number_of_guesses -= 1
                if number < guessed_number:
                    print("You guessed higher!")
                else:
                    print("You guessed lower!")
    elif level_diff == 3:
        number_of_guesses = 10
        print("You get 10 attempts to get the number right")
        while guessed_number != number and number_of_guesses != 0:
            get_guess = int(input("What is your guess? "))
            guessed_number = get_guess
            if guessed_number != number:
                number_of_guesses -= 1
                if number < guessed_number:
                    print("You guessed higher!")
                else:
                    print("You guessed lower!")

    if number_of_guesses == 0 and guessed_number != number:
        print(f"You ran out of guesses. The number was {number}!")
    else:
        print(f"You guessed {guessed_number} and it is correct!")


go_again = 1
while go_again == 1:
    print("Welcome to the number guessing game!")
    number_to_guess = int(random_number_by_pc())
    difficulty = int(input("What difficulty do you want this game to be? Type 1 for hard, 2 for medium, or 3 for easy ->"))
    if difficulty == 1:
        game_loop(1, number=number_to_guess)
    elif difficulty == 2:
        game_loop(2, number=number_to_guess)
    elif difficulty == 3:
        game_loop(3, number=number_to_guess)
    restart = input("Do you want to start over? Yes or No?")
    if restart.lower().strip() == "yes":
        go_again = 1
    else:
        go_again = 0
