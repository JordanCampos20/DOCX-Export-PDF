from pathlib import Path
import docx2pdf

default_folder = f"{Path(__file__).parents[1].resolve()}"

def convert(input, output):
    input_name, input_ext = input.split(".")
    output_name, output_ext = output.split(".")
    try:
        docx2pdf.convert(f"{default_folder}\\{input_name}.{input_ext}", f"{default_folder}\\{output_name}.{output_ext}")
    except Exception as ex:
        raise ex