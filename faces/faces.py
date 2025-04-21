smiley1 = "Hello 🙂"
smiley2 = "Goodbye 🙁"

def main():
    user_input = input()
    output = ""
    if ":)" in user_input:
        output += smiley1
    if ":(" in user_input:
        output += " " + smiley2
    print(output)

main()
