import tkinter
from tkinter import filedialog

def getOpenFileName():
    return tkinter.filedialog.askopenfilename()

def openFile(Name):
    if not isinstance(Name, str):
        raise ValueError("Name should be a string")
    return open(Name)
