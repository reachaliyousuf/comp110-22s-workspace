"""EX01 - Chardle - A cute step toward Wordle."""
    
__author__ = "730243919"

from tokenize import single_quoted


word_choice = input("Enter a 5-character word: ")
if len(word_choice) != 5:
    print("Error: Word must contain 5 characters")
    quit()

single_letter_choice = input("Enter a single character: ")
if len(single_letter_choice) != 1:
    print("Error: Character must be a single character")
    quit()

print("Searching for " + single_letter_choice + " in " + word_choice)

num_of_indices: int = 0

if single_letter_choice == word_choice[0]:
    print(single_letter_choice + " found at index 0")
    num_of_indices = num_of_indices + 1
if single_letter_choice == word_choice[1]:
    print(single_letter_choice + " found at index 1")
    num_of_indices = num_of_indices + 1
if single_letter_choice == word_choice[2]:
    print(single_letter_choice + " found at index 2")
    num_of_indices = num_of_indices + 1
if single_letter_choice == word_choice[3]:
    print(single_letter_choice + " found at index 3")
    num_of_indices = num_of_indices + 1
if single_letter_choice == word_choice[4]:
    print(single_letter_choice + " found at index 4")
    num_of_indices = num_of_indices + 1

if num_of_indices > 0:
    if num_of_indices >= 2:
        print(str(num_of_indices) + " instances of " + single_letter_choice + " found in " + word_choice)
    else:
        print(str(num_of_indices) + " instance of " + single_letter_choice + " found in " + word_choice)
else:
    print("No instances of " + single_letter_choice + " found in " + word_choice)


