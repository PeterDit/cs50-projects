def main():
    time = input("What time is it? ")
    x = convert(time)

    if 7 <= x <= 8:
       print("breakfast time")
    elif 12 <= x <= 13:
        print("lunch time")
    elif 18 <= x <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()
