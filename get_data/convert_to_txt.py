""" 
Convert from .docx file to .txt file
"""
import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return fullText

if __name__ == "__main__":
    text_docx = getText("/content/file-24-ok.docx")
    print(len(text_docx))