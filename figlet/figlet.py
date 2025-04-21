from pyfiglet import Figlet
import sys

figlet = Figlet()

# Check if there are exactly three arguments and if the first argument is "-f"
if len(sys.argv) == 3 and sys.argv[1] == "-f":
    # Check if the provided font (sys.argv[2]) is in the list of available fonts
    if sys.argv[2] in figlet.getFonts():
        font_name = sys.argv[2]
        figlet.setFont(font=font_name)
        user = input("Input: ")
        print(figlet.renderText(user))
    else:
        print("Font not found. Exiting...")
        sys.exit(1)  # Exit with a status code of 1 indicating an error
else:
    print("Incorrect usage. Exiting...")
    sys.exit(1)  # Exit with a status code of 1 indicating an error

# If everything is successful, you can explicitly exit with a status code of 0 (optional)
sys.exit(0)
