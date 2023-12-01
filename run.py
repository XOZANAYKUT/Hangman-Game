import os
import random
from colorama import Fore, Style

# Hangman stages for drawing the gallows
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\ |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\ |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\ |
      / \\ |
           |
    """
]

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_question_and_word(chosen_item, guessed_letters):
    """Displays the question and the word with correctly guessed letters."""
    print(f"Question: {chosen_item['question']}" if 'question' in chosen_item else f"Hint: {chosen_item['hint']}")
    
    if 'answer' in chosen_item:
        displayed_word = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_item['answer'])
        print(f"Word: {displayed_word}")

def choose_item(category):
    """Chooses and returns a general knowledge or computer science item."""
    if category == 1:  # If General Knowledge category is chosen
        items = [
            {"question": "What is the capital of France?", "answer": "paris", "hint": "The city of love"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "shakespeare", "hint": "A famous playwright"},
            {"question": "What is the largest planet in our solar system?", "answer": "jupiter", "hint": "Named after the king of the gods"},
            {"question": "What is the largest mammal on Earth?", "answer": "blue whale", "hint": "It's a marine animal"},
            {"question": "What is the currency of Japan?", "answer": "yen", "hint": "Three letters, starts with 'y'"}
        ]
    elif category == 2:  # If Computer Science category is chosen
        items = [
    {"question": "What is a variable?", "answer": "identifier", "hint": "Used to store data"},
    {"question": "What is the file extension for a Python script?", "answer": "py", "hint": "Two letters"},
    {"question": "Who developed the C programming language?", "answer": "kernighan", "hint": "Co-author of 'The C Programming Language'"},
    {"question": "What is the primary purpose of a compiler?", "answer": "translate", "hint": "Converts high-level code to machine code"},
        ]
    else:
        raise ValueError("Invalid category choice.")

    chosen_item = random.choice(items)
    return chosen_item

def ask_question(chosen_item):
    """Asks a general knowledge or computer science question and returns True if the answer is correct, False otherwise."""
    if 'question' in chosen_item:
        user_answer = input(f"Enter your answer:\n").lower()

        if user_answer == chosen_item['answer']:
            print(Fore.GREEN + "Congratulations! You answered the question correctly." + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "Sorry, wrong answer." + Style.RESET_ALL)
            print("\nHint: " + chosen_item['hint'])
            print_question_and_word(chosen_item, set())
            return False
    else:
        # Only displays the question in the Computer Science category, no word guessing
        return True

def draw_hangman(incorrect_attempts):
    """Draws hangman stages based on the number of incorrect attempts."""
    if incorrect_attempts < len(hangman_stages):
        print(hangman_stages[incorrect_attempts])
    else:
        print(Fore.RED + "Error: Exceeded the list of incorrect guess stages." + Style.RESET_ALL)

def choose_category():
    """Asks the user to choose the category of the word."""
    print("Choose a category for the word:")
    print("1. General Knowledge")
    print("2. Computer Science")
    
    while True:
        try:
            choice = int(input("Enter your choice as a number (1 or 2): \n"))
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_hangman():
    """Plays the Hangman game."""
    category = choose_category()

    clear_screen()
    print(Fore.GREEN + "WELCOME TO HANGMAN!" + Style.RESET_ALL)
  
    if category == 1:
        print("Hint: General Knowledge")
    else:
        print("Hint: Computer Science")

    print("Let the game begin...\n")

    guessed_letters = set()
    incorrect_attempts = 0

    chosen_item = choose_item(category)

    while True:
        draw_hangman(incorrect_attempts)
        print_question_and_word(chosen_item, guessed_letters)

        if set(chosen_item.get('answer', '')) == guessed_letters:
            print(Fore.GREEN + f"Congratulations! You correctly guessed the word: {chosen_item['answer']}" + Style.RESET_ALL)
            break

        guess = input("Guess a letter: \n").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed this letter. Try another one.")
            elif guess in chosen_item.get('answer', ''):
                guessed_letters.add(guess)
                if set(chosen_item.get('answer', '')) == guessed_letters:
                    print(Fore.GREEN + f"Congratulations! You correctly guessed the word: {chosen_item['answer']}" + Style.RESET_ALL)
                    break
            else:
                incorrect_attempts += 1
                draw_hangman(incorrect_attempts)

                if incorrect_attempts == len(hangman_stages) - 1:
                    print(f"{Fore.RED}Hangman hanged! You lost. The correct word: {chosen_item.get('answer', '')}{Style.RESET_ALL}")
                    break
        else:
            incorrect_attempts += 1
            draw_hangman(incorrect_attempts)
            print("Invalid input. Please enter a letter.")

    play_again_input = input("Do you want to play again? (Y)es or (N)o? >: \n").lower()
    return play_again_input == "y"

if __name__ == "__main__":
    while play_hangman():
        pass