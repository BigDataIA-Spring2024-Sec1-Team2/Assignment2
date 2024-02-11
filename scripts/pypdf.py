# import urllib.request
# import pypdf as pyPdf

# def download_pdf(url, filename):
#     urllib.request.urlretrieve(url, filename)

# def extract_text_from_pdf(pdf_path):
#     pdf_file = pyPdf.PdfFileReader(open(pdf_path, 'rb'))
#     text = ''
#     for page_num in range(pdf_file.getNumPages()):
#         page = pdf_file.getPage(page_num)
#         text += page.extractText()
#     return text

# def save_text_to_file(text, output_filename):
#     with open(output_filename, 'w', encoding='utf-8') as output_file:
#         output_file.write(text)

# def main():
#     pdf_url = "https://www.cfainstitute.org/-/media/documents/protected/refresher-reading/2024/level2/level2a/RR_2024_L2V1R5_time_series_analysis.pdf"  # Replace with your actual PDF link
#     pdf_filename = "./RR_2024_L2V1R5_time_series_analysis.pdf"
#     output_text_filename = "extracted_text.txt"

#     # download_pdf(pdf_url, pdf_filename)
#     extracted_text = extract_text_from_pdf(pdf_filename)
#     save_text_to_file(extracted_text, output_text_filename)

# if __name__ == "__main__":
#     main()


import PyPDF2

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

def main():
    pdf_path = "./RR_2024_L2V1R5_time_series_analysis.pdf"  # Replace with the actual path to your PDF file
    output_text_filename = "extracted_text.txt"

    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_file(extracted_text, output_text_filename)

if __name__ == "__main__":
    main()
