from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# Set font for the title
pdf.set_font("Arial", size=40)
pdf.cell(0, 10, "CS50 Shirtificate", ln=True, align='C')

# Add image
image_width = 190  
pdf.image("shirtificate.png", x=(210 - image_width) / 2, y=30, w=image_width)

# Add user's name
name = input("Name: ")
pdf.set_text_color(255, 255, 255)  # Set text color to white
pdf.set_font("Arial", size=16)

# Calculate position for the name (adjust x and y as needed)
pdf.set_xy(10, 90)  # Example coordinates, change according to image placement
pdf.cell(0, 10, f"{name} took a CS50 class", ln=True, align='C')

pdf.output("shirtificate.pdf")
print("PDF created.")
