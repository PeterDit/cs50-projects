from cs50 import get_float

quarters = 0
dimes = 0
nickel = 0
pennies = 0


while True:
    try:
        user_input = get_float("Change: ")
        cents = round(user_input * 100)
        if user_input > 0:
            break
    except ValueError:
        print("")

while cents > 0:
    if cents >= 25:
        cents = cents - (25)
        quarters = quarters + 1

    elif cents >= 10:
        cents = cents - (10)
        dimes = dimes + 1

    elif cents >= 5:
        cents = cents - (5)
        nickel = nickel + 1

    elif cents >= 1:
        cents = cents - (1)
        pennies = pennies + 1

print(quarters + dimes + nickel + pennies)
