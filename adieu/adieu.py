import sys

user_input = []

try:
    while True:
        input_line = input("Name: ").strip()
        if input_line:
            names = input_line.split()
            user_input.extend(names)

except EOFError:
    if len(user_input) == 1:
        print(f"Adieu, adieu, to {user_input[0]}")
    elif len(user_input) == 2:
        print(f"Adieu, adieu, to {user_input[0]} and {user_input[1]}")
    elif len(user_input) > 2:
        names_except_last = ', '.join(user_input[:-1])
        last_name = user_input[-1]
        print(f"Adieu, adieu, to {names_except_last}, and {last_name}")
    sys.exit(0)
