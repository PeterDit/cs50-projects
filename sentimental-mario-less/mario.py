while True:
    try:
        userinput = int(input("Height: "))
        if userinput > 0 and userinput < 9:
            break
    except ValueError:
        print("")

for i in range(userinput):
    # Print leading spaces
    for r in range(userinput - i - 1):
        print(" ", end="")

    # Print first set of hashes
    for r in range(i + 1):
        print("#", end="")

    # Print the two spaces
    print("  ", end="")

    # Print second set of hashes
    for r in range(i + 1):
        print("#", end="")

    # Move to the next line
    print()
