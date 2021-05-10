from PyPDF2 import PdfFileReader, PdfFileWriter

input_1 = input("Which pdf file should get a password?: ")
input_pass = input("Type in the new password: ")
input_2 = input("What should be the name of the new file?: ")

outputFile = PdfFileWriter()
pdffile = PdfFileReader(f"{input_1}.pdf")
numOfPages = pdffile.numPages

for i in range(numOfPages):
    page = pdffile.getPage(i)
    outputFile.addPage(page)

password = input_pass

outputFile.encrypt(password)

with open(f"{input_2}.pdf", "wb") as f:
    outputFile.write(f)
