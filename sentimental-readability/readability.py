from cs50 import get_string

input = get_string("Text: ")
splitted = input.split()

# Adds 1 word since it  checks for spaces not for actually words
word = 1
letters = 0
sentence = 0

# Checks for the amount of words in the text (By checking the spaces in between)
for i in input:
    if i == " ":
        word += 1

# Checks for letters if they are alphabetical
for char in input:
    if char.isalpha():
        letters += 1

# Checks for . ! ?
for i in input:
    if i == ".":
        sentence += 1
    elif i == "!":
        sentence += 1
    elif i == "?":
        sentence += 1

# Some formular i dont understand
L = (letters / word) * 100
S = (sentence / word) * 100
index = 0.0588 * L - 0.296 * S - 15.8


# Printing out the difficulty of the text
if index < 1:
    print(f"Before Grade 1")
elif index >= 16:
    print(f"Grade 16+")
else:
    print(f"Grade ", round(index))
