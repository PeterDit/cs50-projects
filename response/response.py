import validators

email = input("What's your email? ").strip().lower()

if validators.email(email):
    print("Valid")
else:
    print("Invalid")
