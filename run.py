# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
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
            {"question": "In which year did World War II end?", "answer": "1945", "hint": "The mid-20th century"},
            {"question": "What is the currency of Japan?", "answer": "yen", "hint": "Three letters, starts with 'y'"}
        ]       