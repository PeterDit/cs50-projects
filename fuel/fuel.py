def convert(fraction):
    try:
        numerator, denominator = fraction.split("/")
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        percentage = (numerator / denominator) * 100
        return int(percentage)  # Ensure it returns an integer
    except ValueError:
        raise ValueError("Invalid input")
    except ZeroDivisionError:
        raise ZeroDivisionError("Division by zero")

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            if percentage > 100:
                continue
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

if __name__ == "__main__":
    main()
