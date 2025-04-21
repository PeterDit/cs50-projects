import random

randomnumberlvl_1 = list(range(0, 10))
randomnumberlvl_2 = list(range(10, 99))
randomnumberlvl_3 = list(range(100, 999))

def main():
    correct_count = 0
    level = get_level()

    for _ in range(10):  # Das Programm stellt 10 Aufgaben
        correct = generate_integer(level)
        if correct:
            correct_count += 1

    print(f"Score: {correct_count}")
    return 0  # Beendet das Programm sauber

def get_level():
    while True:
        try:
            level = int(input("Level 1-3 : "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            print("")

def generate_integer(level):
    if level == 1:
        x = random.choice(randomnumberlvl_1)
        y = random.choice(randomnumberlvl_1)
    elif level == 2:
        x = random.choice(randomnumberlvl_2)
        y = random.choice(randomnumberlvl_2)
    elif level == 3:
        x = random.choice(randomnumberlvl_3)
        y = random.choice(randomnumberlvl_3)

    correct_answer = x + y

    for _ in range(3):  # Der Benutzer hat 3 Versuche
        try:
            answer = int(input(f"{x} + {y} = "))
            while answer == correct_answer:
                return True
            else:
                print("EEE")
        except ValueError:
            continue

    print(f"{x} + {y} = {correct_answer}")
    return False

if __name__ == "__main__":
    main()
