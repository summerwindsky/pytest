import win32com
from win32com.client import Dispatch,constants
w = Dispatch('Word.Application')
w.Visible = 0
w.DisplayAlerts=0
doc = w.Documents.Open("input.doc")
doc.SaveAs("output.docx",FileFormat=12)