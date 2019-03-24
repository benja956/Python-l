from win32com import client as wc
import os,time
root = "E:\\bd\\caozuo\\stu\\ch"
word= wc.Dispatch("word.Application")
def doc2docx():
    for dirpath, dirnames, filenames in os.walk(root):
        time.sleep(3)
        for filepath in filenames:
            time.sleep(3)
            doc = word.Documents.Open(root + filepath)
            time.sleep(3)
            doc.SaveAs(root + filepath.docx, 12)





doc2docx()
