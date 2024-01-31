import os
from PIL import Image
from fpdf import FPDF

pdf = FPDF()
width, height = 0, 0

for i in range(1, 248+1):
    fname = f"python ({i}).png"
    if os.path.exists(fname):
        if i == 1:
            page = Image.open(fname)
            width, height = page.size
            pdf = FPDF(unit='pt', format=[width, height])
        image = fname
        pdf.add_page()
        pdf.image(image, 0, 0, width, height)
    else:
        print("File not found:", fname)
    print("Processed %d" % i)
pdf.output("Converted_out.pdf", "F")
print("Successfully Converted")
