userinput = input("File Name: ")

if ".gif" in userinput:
    print("image/gif")
elif "jpg" in userinput:
    print("image/jpeg")
elif "jpeg" in userinput:
    print("image/jpeg")
elif ".png" in userinput:
    print("image/png")
elif ".pdf" in userinput or ".PDF" in userinput:
    print("application/pdf")
elif ".txt" in userinput:
    print("text/plain")
elif ".zip" in userinput:
    print("application/zip")
else:
    print("application/octet-stream")
