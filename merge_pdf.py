"""
MErge 
"""
from pathlib import Path
from PyPDF2 import PdfFileMerger, PdfFileReader  # pip install PyPDF2

if __name__ == "__main__":
    pdf_dir = Path(__file__).parent / "input_pdf_files"
    print(pdf_dir)
    
    # Define & create output directory
    pdf_output_dir = Path(__file__).parent / "OUPUT"
  #  pdf_output_dir.mkdir(parents=True, exist_ok=True)
    
    # List all pdf files in the input directory
    pdf_files = list(pdf_dir.glob("*.pdf"))
    print(pdf_files)
    
    merger = PdfFileMerger()
    for file in pdf_files:
            merger.append(PdfFileReader(str(file), "rb"))
        
    merger.write(str(pdf_output_dir /"new_pdf.pdf"))
    merger.close()