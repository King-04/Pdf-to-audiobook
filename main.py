import tkinter as tk
from google.cloud import texttospeech

# Set your Google Cloud Platform credentials file path
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/credentials.json'

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

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_pdf_to_audio)
        self.convert_button.pack(pady=10)

    def convert_pdf_to_audio(self):
        pdf_file_path = self.file_entry.get()

        if not pdf_file_path.endswith('.pdf'):
            tk.messagebox.showerror("Error", "Please select a valid PDF file.")
            return

        try:
            # Extract text from PDF (You can use PyPDF2 or pdfplumber here)
            # Replace the following line with your PDF text extraction logic
            pdf_text = "Sample text extracted from PDF."

            # Initialize Text-to-Speech client
            client = texttospeech.TextToSpeechClient()

            # Set the text input to be synthesized
            synthesis_input = texttospeech.SynthesisInput(text=pdf_text)

            # Select the voice type
            voice = texttospeech.VoiceSelectionParams(
                language_code="en-US",
                name="en-US-Wavenet-D",
            )

            # Select the audio file type
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16
            )

            # Perform the text-to-speech conversion
            response = client.synthesize_speech(
                input=synthesis_input, voice=voice, audio_config=audio_config
            )

            # Save the audio file
            audio_file_path = "output.wav"  # Change this path as needed
            with open(audio_file_path, "wb") as out_file:
                out_file.write(response.audio_content)

            tk.messagebox.showinfo("Conversion Complete", f"Audiobook saved at {audio_file_path}")

        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFToAudioConverter(root)
    root.mainloop()
