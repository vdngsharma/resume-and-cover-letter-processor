import tkinter as tk
from tkinter import filedialog
from document_processor import DocumentProcessor

class EntryField:
    def __init__(self, parent, label_text, default_text=""):
        self.label = tk.Label(parent, text=label_text)
        self.label.pack(pady=5)
        self.entry = tk.Entry(parent)
        self.entry.insert(0, default_text)
        self.entry.pack()

    def get_value(self):
        return self.entry.get()

class RadioButton:
    def __init__(self, parent, text, variable, value):
        self.radio_button = tk.Radiobutton(parent, text=text, variable=variable, value=value)
        self.radio_button.pack()

class Button:
    def __init__(self, parent, text, command):
        self.button = tk.Button(parent, text=text, command=command)
        self.button.pack(pady=10)

class CoverLetterApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cover Letter Generator")
        self.geometry("325x550")

        self.data = {}
        self.name_field = self.create_widgets("Name")

        self.create_radio_button()

        self.job_id_field = self.create_widgets("Job ID")
        self.date_field = self.create_widgets("Date")
        self.address_field = self.create_widgets("Address")
        self.job_title_field = self.create_widgets("Job Title")
        self.org_name_field = self.create_widgets("Organization Name")
        self.team_name_field = self.create_widgets("Team Name")
        self.duties_field = self.create_widgets("Duties")

        self.create_button()

        self.message = None


    def create_widgets(self, label):
        return EntryField(self, label)


    def create_radio_button(self):
        self.cover_letter_type = tk.StringVar(self)
        self.cover_letter_type.set("non_technical")
        self.technical_radio = RadioButton(self, "Technical", self.cover_letter_type, "technical")
        self.non_technical_radio = RadioButton(self, "Non-Technical", self.cover_letter_type, "non_technical")


    def create_button(self):
        self.generate_button = Button(self, "Generate Cover Letter", command = self.generate_cover_letter)


    def generate_cover_letter(self):
        if self.message is None:
            self.message = tk.Label(self)
        else:
            self.message.config(text = "")

        self.data["job_id"] = self.job_id_field.get_value()
        self.data['job_title'] = self.job_title_field.get_value()
        self.data['organization_name'] = self.org_name_field.get_value()
        self.data['duties'] = self.duties_field.get_value()
        self.data['team_name'] = self.team_name_field.get_value()
        self.data['address'] = self.address_field.get_value()
        self.data['date'] = self.date_field.get_value()
        self.data['name'] = self.name_field.get_value()
        self.data["type"] = self.cover_letter_type.get()

        status = DocumentProcessor(self.data).save_document()

        if status == True:
            self.message.config(text = "Generated", fg = "green")
        else:    
            self.message.config(text = "Error!", fg = "red")

        self.message.pack()

if __name__ == "__main__":
    app = CoverLetterApp()
    app.mainloop()
