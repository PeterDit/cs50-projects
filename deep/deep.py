getuserinput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
getuserinput = getuserinput.lower()
if "42" in getuserinput or "forty-two" in getuserinput or "forty two" in getuserinput:
    print("Yes")
else:
    print("No")
