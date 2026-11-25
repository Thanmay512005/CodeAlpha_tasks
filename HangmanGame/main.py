import random


def show_word(word, guessed_letters):
    """Show guessed letters and hide the remaining letters."""
    display = []

    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append("_")

    return " ".join(display)


def play_hangman():
    words = ["python", "laptop", "garden", "cricket", "orange"]
    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")

    while wrong_guesses < max_wrong_guesses:
        print("\nWord:", show_word(secret_word, guessed_letters))
        print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            wrong_guesses += 1
            print("That letter is not in the word.")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nYou guessed the word:", secret_word)
            print("You win!")
            return

    print("\nYou are out of guesses.")
    print("The word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
