import random
import webbrowser
import hangman_stages


def gameplay_loop():
    count = 0
    index = 0
    already_guessed = []
    guessed_word = ""
    print("Game started!\n")
    #pseudorandomly picks a word from the txt file
    hangman_word_in_loop = random.choice(open_file.read().split()).strip()
    len_of_word = len(hangman_word_in_loop)
    print("You word has this many symbols: ")
    for _ in range(0, len_of_word):
        #these attributes of the print function make sure that everything is printed on the same line
        #and that there is no space between symbols and that the buffer is cleared afterwards
        print("_", sep='', end='', flush=True)
    #while loop makes sure the game is ongoing until you guess or lose
    while True:
        guess = input("\nChoose vowel or consonant -> ")
        #only one symbol at a time
        if len(guess) > 1:
            print("Please enter a single letter!")
        elif guess in already_guessed:
            print("You already guessed this letter!")
        #the words contain only latin characters, so this makes sure you input the correct symbol
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Must be a letter of latin/English alphabet!")
        else:
            if guess in hangman_word_in_loop:
                print("Correct!")
                for _ in hangman_word_in_loop:
                    index += 1
                    if guess == _:
                        symbol = guess
                        already_guessed.append(symbol)
                        guessed_word += symbol
                    else:
                        symbol = "_"
                        guessed_word += symbol
                print(guessed_word)
                if guessed_word == hangman_word_in_loop:
                    return 1, hangman_word_in_loop
            else:
                print("Incorrect")
                print(hangman_stages.HANGMANPICS[count])
                count += 1
                if count == len(hangman_stages.HANGMANPICS):
                    return 0, hangman_word_in_loop


# open a file handle so that it automatically closes ones done
with open("words_alpha.txt", 'r') as open_file:
    print("Welcome to the game of Hangman!")
    print(hangman_stages.HANGMANPICS[-1])
    tries = len(hangman_stages.HANGMANPICS)
    print("PC at random has picked a word from English language. Can you guess it? It may differ from simple to extra hard.\n"
          f"You have {tries} tries!")
    print("If the hangman picture gets fully drawn you lose!")
    # starts the gameplay loop, this will return the status - loss or win, and the word the PC picked
    status, hangman_word = gameplay_loop()
    if status == 1:
        print(f"Congratulations! You won!\nThe word was {hangman_word}")
    else:
        print(f"You lost!\nThe word was {hangman_word}")
    get_meaning = input("Do you want to get the meaning of this word? Y or N -> ")
    # if the player is interested in playing this will open a google search of that word
    if get_meaning.capitalize() == "Y":
        url = "https://www.google.com/search?q={}".format(hangman_word)
        #concatenate the word meaning to the url, just to make sure we get the meaning of the word and not some brand or smth
        webbrowser.open_new_tab(url + " meaning")
        quit("Game Over")
    else:
        quit("Game Over")
