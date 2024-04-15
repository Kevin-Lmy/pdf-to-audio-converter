from functions import *


def main():
    pdf_file = ""
    while not pdf_file:
        pdf_file = input("PDF file with the file extension: ")
    start_page = input("Start page (Leave blank for the first page): ")
    end_page = input("End page (Leave blank for the Last page): ")
    output_file = input("Audio output file with the file extension: ")

    try:
        extracted_text = ""

        if not start_page and not end_page:
            extracted_text = extract_text_from_pages(pdf_file)
        elif start_page and not end_page:
            extracted_text = extract_text_from_pages(pdf_file, int(start_page))
        elif not start_page and end_page:
            extracted_text = extract_text_from_pages(pdf_file, end_page=int(end_page))
        else:
            extracted_text = extract_text_from_pages(pdf_file, int(start_page), int(end_page))

        convert_text_to_audio(extracted_text, output_file)
    except Exception as e:
        print("An error occurred: ", e)


if __name__ == "__main__":
    main()