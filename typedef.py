


def main():
    hello()
    name = input("whats your name? ")
    hello(name)

#Deffining a function (If no argument is given its printing world)
def hello(to="world"):
    print("hello", to)

"""
x=int(input("whats x", x))
print(square(x))
def square(n):
    return n*n
"""


main()
