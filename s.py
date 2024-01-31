from PyPDF2 import PdfMerger
pdfs = ["report.pdf", "summary.pdf"]
merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged2.pdf")
merger.close()
