import PyPDF2
pdffiles=["Lec-2.pdf","Lec-4.pdf"]
merger=PyPDF2.PdfMerger()
for filename in pdffiles:
    pdfile=open(filename,"rb")
    pdfreader=PyPDF2.PdfReader(pdfile)
    merger.append(pdfreader)
pdfile.close()
merger.write("merged.pdf")
