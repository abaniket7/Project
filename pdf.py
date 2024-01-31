# import os
# from PyPDF2 import PdfWriter
# merger = PdfWriter()
# files = [file for file in os.listdir() if file.endswith(".pdf")]
# for pdf in files:
#     merger.append(pdf)
# merger.write("merged-pdf.pdf")
# merger.close()

# import PyPDF2
# import os
#
# def merge_pdfs(input_dir, output_file):
#     pdf_merger = PyPDF2.PdfFileMerger()
#
#     # Get all PDF files in the input directory
#     pdf_files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]
#
#     # Merge all PDF files
#     for pdf_file in pdf_files:
#         pdf_path = os.path.join(input_dir, pdf_file)
#         pdf_merger.append(pdf_path)
#
#     # Write the merged PDF to the output file
#     with open(output_file, 'wb') as output:
#         pdf_merger.write(output)
#
#     print(f"Merged {len(pdf_files)} PDF files into {output_file}")
#
# # Provide the input directory containing PDF files and the output file path
# input_directory = 'path/to/input/directory'
# output_file_path = 'path/to/output/file.pdf'
#
# # Call the function to merge PDF files
# merge_pdfs(input_directory, output_file_path)


from PyPDF2 import PdfMerger
pdfs = ["report.pdf", "summary.pdf"]
merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("merged2.pdf")
merger.close()
