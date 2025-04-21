"""
Ask user for their name and greet em
name = input("What's your name: ")
"""



#You can also do this (add to the end)
name = input("What's your name: ").strip().title()

#Split users name into first and last name
first, last = name.split(" ")

"""
# Remove white space from str (name)
name = name.strip()

#Capitalize first word
name = name.capitalze()

# Capitalize ever word
name = name.title()
"""

# Print the the first input given or last
print(f"Hi, {last}")
