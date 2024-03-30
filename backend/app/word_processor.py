from docx import Document


class WordProcessor:

    def __init__(self, file_path):
        self.doc = Document(file_path)

    def find_replace(self, target, replacement):
        for paragraph in self.doc.paragraphs:
            if target in paragraph.text:
                paragraph.text = paragraph.text.replace(target, replacement)

            for run in paragraph.runs:
                if target in run.text:
                    run.text = run.text.replace(target, replacement)

    def save_document(self, output_path):
        self.doc.save(output_path)

word_processor = WordProcessor('..\\cover-letters\\non_technical_cover_letter.docx')

target_word = '[JOB TITLE]'
replacement_word = 'KADDU'

word_processor.find_replace(target_word, replacement_word)

word_processor.save_document('..\\cover-letters\\new_cover_letter.docx')

