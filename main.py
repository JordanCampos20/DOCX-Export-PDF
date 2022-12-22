import docx2pdf
import sys

def convert(input, output):
    docx2pdf.convert(input, output)
    
if __name__ == "__main__":
    inp = str(sys.argv[1])
    out = str(sys.argv[2])
    convert(inp, out)