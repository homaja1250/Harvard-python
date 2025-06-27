
from fpdf import FPDF

def create_shirtificate(name):
    pdf = FPDF(orientation='P', format='A4')
    pdf.add_page()

    # Add title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt='CS50 Shirtificate', ln=True, align='C')

    # Add shirt image
    pdf.image('shirtificate.png', x=50, y=20, w=110)

    # Add user name
    pdf.set_font('Arial', '', 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=90, y=70, txt=name)

    pdf.output('shirtificate.pdf')

name = input("Enter your name: ")
create_shirtificate(name)
