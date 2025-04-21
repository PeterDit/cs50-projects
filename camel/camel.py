user_input = input("camelCase: ")
result = ""

for char in user_input:
    if char.isupper():
        result += "_" + char.lower()
    else:
        result += char

print(result)
