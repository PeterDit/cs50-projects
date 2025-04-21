import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

input_filename = sys.argv[1]  # Input image (e.g., before1.jpg)
output_filename = sys.argv[2]  # Output image (e.g., after1.jpg)

# Extract file extensions
input_ext = os.path.splitext(input_filename)[1].lower()
output_ext = os.path.splitext(output_filename)[1].lower()

# Check if the input file has a valid image extension
if not (input_ext == ".jpg" or input_ext == ".png"):
    print("Input file is not a valid image (.jpg or .png)")
    sys.exit(1)

if not os.path.isfile(input_filename):
    print("Input does not exist")
    sys.exit(1)


# Check if the output file has a valid image extension
if not (output_ext == ".jpg" or output_ext == ".png"):
    print("Output file is not a valid image (.jpg or .png)")
    sys.exit(1)

# Ensure input and output extensions match
if input_ext != output_ext:
    print("Input and output have different extensions")
    sys.exit(1)

# Now proceed with your image manipulation
try:
# Open input image and shirt overlay
    with Image.open(input_filename) as img:
        with Image.open("hat.png") as shirt:
            # Resize and crop the input image to fit the shirt's size
            fitted_img = ImageOps.fit(img, shirt.size)
            fitted_img = fitted_img.convert("RGBA")
            shirt = shirt.convert("RGBA")

            # Paste the shirt image onto the fitted input image
            fitted_img.paste(shirt, (0, 0), shirt)

            # Convert fitted_img to RGB if saving as JPEG
            if output_ext == ".jpg":
                fitted_img = fitted_img.convert("RGB")

            # Save the result to the output filename with appropriate format
            fitted_img.save(output_filename, format="JPEG" if output_ext == ".jpg" else "PNG")
            print(f"Image saved as {output_filename}")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
