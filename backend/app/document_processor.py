import os
from dotenv import dotenv_values
from docx import Document
from docx2pdf import convert

class DocumentProcessor:

    def __init__(self, data):
        print(data)
        self.env_vars = dotenv_values('.env')
        self.target_word = data.get('target_word')
        self.replacement_word = data.get('replacement_word')
        self.name = '_'.join(self.env_vars.get('NAME').split())
        self.job_id = data.get('job_id')
        type_ = data.get('type')

        if type_ == 'nonTechnical': 
            self.doc = Document(self.env_vars.get('NON_TECHNICAL_COVER_LETTER_PATH'))
        else:
            self.doc = Document(self.env_vars.get('TECHINCAL_COVER_LETTER_PATH'))
        

    def process_document(self):
        for paragraph in self.doc.paragraphs:
            if self.target_word in paragraph.text:
                paragraph.text = paragraph.text.replace(self.target_word, self.replacement_word)

            for run in paragraph.runs:
                if self.target_word in run.text:
                    run.text = run.text.replace(self.target_word, self.replacement_word)

        self.save_document()
        

    def save_document(self):
        directory_name = self.job_id
        parent_directory_path = self.env_vars.get('SAVE_DIRECTORY_PATH')
        save_directory_path = os.path.join(parent_directory_path, directory_name)
        if not os.path.exists(save_directory_path):
            os.makedirs(save_directory_path)

        file_name = self.name + '_' + directory_name + '_Cover_Letter.docx'
        file_save_path = os.path.join(save_directory_path, file_name)

        self.doc.save(file_save_path)
        convert(file_save_path)
