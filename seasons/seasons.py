from datetime import date, datetime
import inflect
import sys

p = inflect.engine()

def get_birth_date(user_input=None):
    if user_input is None:
        user_input = input("Date of Birth (YYYY-MM-DD): ").strip()
    try:
        birth_date = datetime.strptime(user_input, "%Y-%m-%d").date()
        return birth_date
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)
        
def calculate_minutes(birth_date):
    today = date.today()
    difference = today - birth_date
    return difference.total_seconds() / 60

def convert_to_words(minutes):
    words = p.number_to_words(int(round(minutes)))
    words = words.replace(" and", "")
    return words.capitalize()
def main():
    birth_date = get_birth_date()
    minutes = calculate_minutes(birth_date)
    minutes_in_words = convert_to_words(minutes)
    print(f"{minutes_in_words} minutes")

if __name__ == "__main__":
    main()
