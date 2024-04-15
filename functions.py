import PyPDF2
import gtts


def extract_text_from_pages(pdf_path, start_page=None, end_page=None):
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        
        total_pages = len(pdf_reader.pages)
        start_page = start_page if start_page else 1
        end_page = end_page if end_page else total_pages

        extracted_text = ""

        for page_num in range(start_page-1, end_page):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

        return extracted_text
    
def convert_text_to_audio(text, output_file):
    gtts.gTTS(text, "com.au", "en").save(output_file)