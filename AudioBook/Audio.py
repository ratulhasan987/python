import pyttsx3
import PyPDF2
book = open('django.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
audio = pyttsx3.init()
for num in range(6, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    audio.say(text)
    audio.runAndWait()