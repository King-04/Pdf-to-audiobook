import tkinter as tk
from tkinter import filedialog
import pdfplumber
import pyttsx3

class PDFToAudioConverter:
    def __init__(self, master):
        self.master = master
        master.title("PDF to Audiobook Converter")

        self.label = tk.Label(master, text="PDF to Audiobook Converter", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.file_label = tk.Label(master, text="Select PDF File:")
        self.file_label.pack()

        self.file_entry = tk.Entry(master, width=50)
        self.file_entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_pdf)
        self.browse_button.pack(pady=5)

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_pdf_to_audio)
        self.convert_button.pack(pady=10)

    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(tk.END, file_path)

    def convert_pdf_to_audio(self):
        pdf_file_path = self.file_entry.get()

        if not pdf_file_path.endswith('.pdf'):
            tk.messagebox.showerror("Error", "Please select a valid PDF file.")
            return

        try:
            # Extract text from PDF using pdfplumber
            pdf_text = ""
            with pdfplumber.open(pdf_file_path) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text()

            # Initialize pyttsx3 engine
            engine = pyttsx3.init()

            # Perform the text-to-speech conversion
            engine.save_to_file(pdf_text, "./output.mp3")  # Change the file extension as needed
            engine.runAndWait()

            tk.messagebox.showinfo("Conversion Complete", "Audiobook saved at output.mp3")

        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToAudioConverter(root)
    root.mainloop()
