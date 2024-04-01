import os
import comtypes
from docx import Document
from docx2pdf import convert
from dotenv import dotenv_values


class DocumentProcessor:

    def __init__(self, data):
        self.env_vars = dotenv_values('.env')

        self.name = self.env_vars.get('NAME')
        self.job_id = data.get('jobId')
        self.type_ = data.get('type')
        self.data = data

        template_path = self.env_vars.get('NON_TECHNICAL_COVER_LETTER_PATH') if self.type_ == 'nonTechnical' else self.env_vars.get('TECHNICAL_COVER_LETTER_PATH')
        self.doc = Document(template_path)

        placeholders = {
            '[DATE]': 'date',
            '[SENDER\'S ADDRESS]': 'address',
            '[JOB TITLE]': 'jobTitle',
            '[ORGANIZATION NAME]': 'organizationName',
            '[TEAM NAME]': 'teamName',
            '[DUTIES]': 'duties'
        }

        for placeholder, key in placeholders.items():
            self.process_document(placeholder, data.get(key))

        self.save_document()

    def process_document(self, target_word, replacement_word):
        for paragraph in self.doc.paragraphs:
            if target_word in paragraph.text:
                paragraph.text = paragraph.text.replace(target_word, replacement_word)

                if target_word == '[SENDER\'S ADDRESS]':
                    parts = replacement_word.split(', ')
                    formatted_address = ',\n'.join(parts)
                    paragraph.text = formatted_address

            for run in paragraph.runs:
                if target_word in run.text:
                    run.text = run.text.replace(target_word, replacement_word)
        

    def save_document(self):
        directory_name = self.job_id

        parent_directory_path = self.env_vars.get('SAVE_DIRECTORY_PATH')

        save_directory_path = os.path.join(parent_directory_path, directory_name)
        if not os.path.exists(save_directory_path):
            os.makedirs(save_directory_path)

        name = '_'.join(self.name.split())
        docx_file_name = name + '_' + directory_name + '_Cover_Letter.docx'
        docx_file_save_path = os.path.join(save_directory_path, docx_file_name)

        pdf_file_name = name + '_' + directory_name + '_Cover_Letter.pdf'
        pdf_file_save_path = os.path.join(save_directory_path, pdf_file_name)

        self.doc.save(docx_file_save_path)

        if os.path.isfile(pdf_file_save_path):
            os.remove(pdf_file_save_path)
            comtypes.CoInitialize()
            
        convert(docx_file_save_path)
            