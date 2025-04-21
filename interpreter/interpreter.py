expression = input("Expression: ")

x, y, z = expression.split(" ")

x = int(x)
z = int(z)

if y == "+":
    result = float(x) + float (z)
elif y == "-":
    result = float(x) - float(z)
elif y == "*":
    result = float(x) * float(z)
elif y == "/":
    result = float(x) / float(z)

print(result)
