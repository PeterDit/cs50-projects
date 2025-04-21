def main():
    userin = input("Input: ")
    shortened = shorten(userin)
    print("Output:", shortened)

def shorten(word):
    result = ""
    for char in word:
        if char not in "aeiouAEIOU":
            result += char
    return result

if __name__ == "__main__":
    main()
