import re

def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    match = re.match(r"(\d{1,2})(?::(\d{2}))? ([AP]M) to (\d{1,2})(?::(\d{2}))? ([AP]M)", s)

    if not match:
        raise ValueError("")

    hour1, minute1, period1, hour2, minute2, period2 = match.groups()

    minute1 = minute1 if minute1 else "00"
    minute2 = minute2 if minute2 else "00"

    if not (0 <= int(minute1) < 60) or not (0 <= int(minute2) < 60):
        raise ValueError()

    time1 = to_24_hour_format(int(hour1), int(minute1), period1)
    time2 = to_24_hour_format(int(hour2), int(minute2), period2)

    return f"{time1} to {time2}"


def to_24_hour_format(hour, minute, period):
    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0
    return f"{hour:02}:{minute:02}"  # Return time in 24-hour format

if __name__ == "__main__":
    main()
