import re

email = input("What's your email? ").strip().lower()

# or ..* instead of .+. Using \ so .edu can be searched as text
#The ^ and $ makes sure for excact input
# \w = [1-9a-zA-Z_] = word character,numbers and underscore
            #(r"^)+@(\w+\.)?\w+\.edu$)"
if re.search(r"^[a-z0-9_\.]+@\w+\.(com|edu|net|de)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
