from cs50 import get_string


def checkLuhn(input):
    number = len(input)
    nSum = 0
    isSecond = False

    for i in range(number - 1, -1, -1):
        d = ord(input[i]) - ord("0")
        if isSecond:
            d *= 2
        nSum += d // 10
        nSum += d % 10
        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False


while True:
    input = get_string("Number: ")
    if checkLuhn(input):
        length = len(input)
        if length == 15 and (input.startswith("34") or input.startswith("37")):
            print("AMEX")
            break
        elif length == 16 and (input.startswith("51") or input.startswith("52") or input.startswith("53") or input.startswith("54") or input.startswith("55")):
            print("MASTERCARD")
            break
        elif (length == 13 or length == 16) and input.startswith("4"):
            print("VISA")
            break
        else:
            print("INVALID")
            break
    else:
        print("INVALID")
        break
