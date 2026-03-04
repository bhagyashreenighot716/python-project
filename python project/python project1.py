import json
from difflib import get_close_matches

with open("data.json") as file:
    data = json.load(file)

def find_meaning(word):
    word = word.lower()

    if word in data:
        return data[word]

    close_matches = get_close_matches(word, data.keys(), n=1, cutoff=0.6)

    if close_matches:
        suggestion = close_matches[0]
        choice = input(f"Did you mean '{suggestion}'? (Y/N): ")

        if choice.lower() == "y":
            return data[suggestion]
        else:
            return "Word not found."

    return "Word not found."

print("📖 English Dictionary Application")
print("Type 'exit' to quit.\n")

while True:
    user_word = input("Enter a word: ")

    if user_word.lower() == "exit":
        print("Thank you for using the Dictionary App!")
        break

    meaning = find_meaning(user_word)
    print("Meaning:", meaning)
    print()