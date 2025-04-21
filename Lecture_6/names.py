names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted (names, reverse=True):
    print(f"hello,{name}")


   #.append is adding name to the dict []

    # sorted is sorting the names in the list

    # end="" or .rstrip cuts of the line in between
