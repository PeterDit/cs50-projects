import random

while True:
    try:
        lvluser = int(input("Level: "))
        if 1 <= lvluser <= 10:
            random_number = random.randint(1, lvluser)
            while True:
                try:
                    guessuser = int(input(f"Guess: "))
                    if guessuser > random_number:
                        print("Too large!")
                    elif guessuser < random_number:
                        print("Too small!")
                    else:
                        print("Just Right!")
                        break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            break
        else:
            print("Too large!")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
