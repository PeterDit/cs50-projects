def get_guess():
    guess = input("Enter a Guess:")
    return guess

def main():
    guess = get_guess()
    if guess == "car":
        print("Correct!")
    else:
        print("Incorrect!")

main()

