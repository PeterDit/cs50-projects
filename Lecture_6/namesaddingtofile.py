name = input ("What's your name? ")

#Creates a file called names.txt, "a" adds names to the list, instead of over printing
file = open ("names.txt", "a")
file.write(f"{name}\n")
file.close()

#.append is adding name to the dict []

    # sorted is sorting the names in the list

    # end="" or .rstrip cuts of the line in between
