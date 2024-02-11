import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text

def save_text_to_file(text, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

def process_pdfs_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory_path, filename)
            output_text_filename = f"{os.path.splitext(filename)[0]}.txt"

            extracted_text = extract_text_from_pdf(pdf_path)
            save_text_to_file(extracted_text, output_text_filename)
            print(f"Text extracted and saved to {output_text_filename}")

def main():
    pdfs_directory_path = "C:/Users/aptea/OneDrive/Documents/NEU/Sem6/BDIA/Assignment 2/Archive 2"  # Replace with the actual path to your directory containing PDFs
    process_pdfs_in_directory(pdfs_directory_path)

if __name__ == "__main__":
    main()
