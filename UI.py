from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import datetime

NAME = "PC Covid"

def Window():
    global tab1, tab2, copyrightFrame
    bigframe = ttk.Frame(root)
    bigframe.pack(fill=tk.BOTH, expand=1)

    notebook = ttk.Notebook(bigframe)
    notebook.pack(fill=tk.BOTH, expand=1)

    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Tab 1")

    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="Tab 2")

def Global():
    global resultFrameGlobal
    resultFrameGlobal = ttk.LabelFrame(tab1, text="Total Information")
    resultFrameGlobal.pack(fill=tk.BOTH, expand=1, padx=10, pady=5)

    copyrightFrame = ttk.Frame(tab1)
    copyrightFrame.pack(fill=tk.X, expand=1, padx=10, pady=0)

    label = ttk.Label(copyrightFrame, text="Copyright © 2021 by Khoa Nguyen")
    label.pack(padx=10, pady=0, side=BOTTOM)

    GlobalData()

def GlobalData():
    globalTitle = ttk.Label(resultFrameGlobal, text="Vietnam Covid19 Information", font=("Arial", 13, BOLD))
    globalTitle.pack(side=TOP, padx=10, pady=(10,0))

    seperator = ttk.Separator(resultFrameGlobal, orient=tk.HORIZONTAL)
    seperator.pack(fill=tk.X, padx=10, pady=10)

    globalData = ttk.Label(resultFrameGlobal, text=
    "Total cases: " + "\n"  
    "Total deaths: " + "\n" 
    "Total recovered: " + "\n" 
    "Total active: ")
    globalData.pack(padx=10, pady=3)

    globalData2 = ttk.Label(resultFrameGlobal, text=
    "New cases: " + "\n"  
    "New deaths: " + "\n" 
    "New recovered: ")
    globalData2.pack(padx=10, pady=3)

def City():
    global resultFrame, entry
    resultFrame = ttk.LabelFrame(tab2, text="Covid19 Application")
    resultFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=(10,0))

    interactFrame = ttk.LabelFrame(tab2, text="Entry")
    interactFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=0)

    copyrightFrame = ttk.Frame(tab2)
    copyrightFrame.pack(fill=tk.X, expand=1, padx=10, pady=0)

    entry = ttk.Entry(interactFrame)
    entry.pack(side=LEFT, padx=10, pady=3)

    searchButton = ttk.Button(interactFrame, text="Search", style="Accent.TButton")
    searchButton.pack(side=LEFT,padx=10, pady=10)

    label = ttk.Label(copyrightFrame, text="Copyright © 2021 by Khoa Nguyen")
    label.pack(padx=10, pady=10, side=BOTTOM)
    DataCity()

def DataCity():
    city = entry.get()
    globalTitle = ttk.Label(resultFrame, text= city + "Covid19 Information", font=("Arial", 13, BOLD))
    globalTitle.pack(side=TOP, padx=10, pady=(10,0))

    seperator = ttk.Separator(resultFrame, orient=tk.HORIZONTAL)
    seperator.pack(fill=tk.X, padx=10, pady=10)

    globalData2 = ttk.Label(resultFrame, text=
    "New cases: " + "\n"  
    "New deaths: " + "\n" 
    "New recovered: ")
    globalData2.pack(padx=10, pady=10)

def App():
    Window()
    Global()
    City()

if __name__ == "__main__":
    root = tk.Tk()
    root.title(NAME)
    root.geometry("300x330")
    root.resizable(False, False)

    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    App()

    root.mainloop()