import re

user_cash_amount = 100000  # Cash
coin_names = ["Bitcoin", "Ethereum", "Solana"]
coin_prices = [57971, 2354, 133]  # Prices for BTC, ETH, SOL (13.09.2024)
user_coins = [0, 0, 0]  # Amount of each coin the user owns (BTC, ETH, SOL)


# Removes special characters
def clean_input(user_input):
    # Removes all non-alphanumeric characters
    return re.sub(r"[^A-Za-z0-9 ]+", "", user_input)


def validate_name(name):
    return bool(re.match("^[A-Za-z ]*$", name))  # Only letters and spaces


def main():
    while True:
        print("Welcome to the Cryptocurrency Market simulation!")
        start = input("Type 'Start' to continue or 'Exit' to quit: ").lower()
        start = clean_input(start)

        if start == "start":
            name = input("What's your name? ")
            name = clean_input(name)

            if validate_name(name):
                choose_action(name)
            else:
                print("Invalid characters in the name. Please try again.")
        elif start == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'Start' or 'Exit'.")


def choose_action(name):
    global user_cash_amount

    while True:
        print(f"\nHi {name}, your current balance is ${user_cash_amount}.")
        print("---------------------------------------------------")
        print("1. Buy\n2. Sell\n3. Check Balance\n4. Exit")
        action = input("Please choose an action (1/2/3/4): ")
        action = clean_input(action)
        print("---------------------------------------------------")

        if action == "1":
            choose_coin(name, "buy")
        elif action == "2":
            choose_coin(name, "sell")
        elif action == "3":
            check_balance(name)
        elif action == "4":
            print("Exiting...")
            break  # Exit the programm
        else:
            print("Invalid action. Please choose again.")


def choose_coin(name, action_type):
    while True:
        print("Choose a cryptocurrency:")
        print("1. Bitcoin\n2. Ethereum\n3. Solana")
        print("-----------------------------------------------------")
        coin_choice = input("Enter the number (1/2/3) of the coin you want: ")
        coin_choice = clean_input(coin_choice)
        print("-----------------------------------------------------")

        if coin_choice in ["1", "2", "3"]:
            coin_index = int(coin_choice) - 1
            if action_type == "buy":
                buy_coin(name, coin_index)
            elif action_type == "sell":
                sell_coin(name, coin_index)
            break  # Exit the loop
        else:
            print("Invalid coin selection. Please try again.")


def buy_coin(name, coin_index):
    global user_cash_amount
    coin_price = coin_prices[coin_index]

    print(f"Buying {coin_names[coin_index]} at ${coin_price} per coin.")
    while True:
        amount_str = input(
            f"How much of {coin_names[coin_index]} would you like to buy? (In dollars): "
        )
        amount_str = clean_input(amount_str)
        print("-----------------------------------------------------")

        try:
            amount = float(amount_str.replace(",", "."))
            if amount <= user_cash_amount:
                bought_coins = amount / coin_price
                user_coins[coin_index] += bought_coins
                user_cash_amount -= amount
                print(
                    f">>> You have successfully bought {bought_coins:.6f} {coin_names[coin_index]}. <<<"
                )
            else:
                print("Not enough balance.")
            break  # Exit the loop after a successful or failed transaction
        except ValueError:
            print("Invalid amount entered. Please enter a valid number.")

    print(f">>> New balance: ${user_cash_amount} <<<")


def sell_coin(name, coin_index):
    global user_cash_amount
    coin_price = coin_prices[coin_index]

    print(f"Selling {coin_names[coin_index]} at ${coin_price} per coin.")
    # Calculate the dollar value of the coins
    owned_coins_value = user_coins[coin_index] * coin_price
    print(
        f"You own {user_coins[coin_index]:.6f} {coin_names[coin_index]}, worth ${owned_coins_value:.2f}."
    )

    while True:
        amount_str = input(
            f"How much {coin_names[coin_index]} would you like to sell? (In dollars): "
        )
        amount_str = clean_input(amount_str)
        print("-----------------------------------------------------")

        try:
            amount_in_dollars = float(amount_str.replace(",", "."))
            coins_to_sell = amount_in_dollars / coin_price

            # Check if the user has enough coins to cover the sale
            if coins_to_sell <= user_coins[coin_index]:
                user_coins[coin_index] -= coins_to_sell
                user_cash_amount += amount_in_dollars
                print(
                    f">>> You have sold ${amount_in_dollars:.2f} worth of {coin_names[coin_index]} ({coins_to_sell:.6f} coins). <<<"
                )
            else:
                print("Not enough coins to sell.")
            break  # Exit the programm
        except ValueError:
            print("Invalid amount entered. Please enter a valid number.")

    print(f">>> New balance: ${user_cash_amount} <<<")


def check_balance(name):
    print(f"Hi {name}, here are your current balances:")
    print(f"Cash balance: ${user_cash_amount}")
    print(f"Bitcoin (BTC): {user_coins[0]:.6f}")
    print(f"Ethereum (ETH): {user_coins[1]:.6f}")
    print(f"Solana (SOL): {user_coins[2]:.6f}")


if __name__ == "__main__":
    main()
