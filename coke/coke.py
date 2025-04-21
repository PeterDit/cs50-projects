amount_due = 50

while amount_due > 0:
    coin_input = int(input("Insert Coin: "))
    if coin_input in [5,10,25,50]:
        amount_due -= coin_input
        if amount_due > 0:
            print("Amount Due:", amount_due)
        elif amount_due == 0:
            print("Change Owed:", amount_due)
        else:
            print("Change Owed:", -amount_due)
    else:
        print("Amount Due:", amount_due)
