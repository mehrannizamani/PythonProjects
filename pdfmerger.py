import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_cominer (pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('super.pdf')

pdf_cominer(inputs)