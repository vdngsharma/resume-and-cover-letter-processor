import tkinter as tk
from tkinter import filedialog
# from your_script import DocumentProcessor  # Replace with the actual path to your script
from document_processor import DocumentProcessor

class EntryField:
    def __init__(self, parent, label_text, default_text=""):
        self.label = tk.Label(parent, text=label_text)
        self.label.pack(pady=10)
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
        self.geometry("325x525")

        self.data = {}
        self.create_radio_button()

        self.job_id_field = self.create_widgets("Job ID")
        self.date_field = self.create_widgets("Date")
        self.address_field = self.create_widgets("Address")
        self.job_title_field = self.create_widgets("Job Title")
        self.org_name_field = self.create_widgets("Organization Name")
        self.team_name_field = self.create_widgets("Team Name")
        self.duties_field = self.create_widgets("Duties")

        self.create_button()


    def create_widgets(self, label, width = None, height = None):
        return EntryField(self, label)


    def create_radio_button(self):
        self.cover_letter_type = tk.StringVar(self)
        self.cover_letter_type.set("nonTechnical")  # Default selection
        self.technical_radio = RadioButton(self, "Technical", self.cover_letter_type, "technical")
        self.non_technical_radio = RadioButton(self, "Non-Technical", self.cover_letter_type, "nonTechnical")


    def create_button(self):
        self.generate_button = Button(self, "Generate Cover Letter", command=self.generate_cover_letter)


    def generate_cover_letter(self):
        self.data["job_id"] = self.job_id_field.get_value()
        self.data['job_title'] = self.job_title_field.get_value()
        self.data['organization_name'] = self.org_name_field.get_value()
        self.data['duties'] = self.duties_field.get_value()
        self.data['team_name'] = self.team_name_field.get_value()
        self.data['address'] = self.address_field.get_value()
        self.data['date'] = self.date_field.get_value()
        self.data["type"] = self.cover_letter_type.get()

        DocumentProcessor(self.data)

        message = tk.Label(self, text="Cover Letter Generated Successfully!", fg="green")
        message.pack()

if __name__ == "__main__":
    app = CoverLetterApp()
    app.mainloop()
