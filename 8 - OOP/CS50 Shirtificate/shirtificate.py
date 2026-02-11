from fpdf import FPDF

name = input("Name: ")
pdf = FPDF()    #creating a pdf object -- default values assumed (orientation="P", unit="mm", format="A4")

pdf.add_page()  #adding a page to the pdf
pdf.set_font("Courier", style="B", size=50)   #these must be defined before adding text to the pdf. b=bold, symbold=font
pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')  #create text box
pdf.image("shirtificate.png", w = pdf.epw) #add the shirt image png. second parameter: width of new image = our pdf . 'effective page width'. ie, stretch image out to same width of our current pdf
pdf.set_font_size(20)
pdf.set_text_color(255,255,255) #parameters red.green.blue. 255 in each = white
pdf.text(x=45, y=150, text = f"{name} took CS50")


pdf.output("shirtificate.pdf") #close and save pdf
