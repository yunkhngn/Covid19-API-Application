from tkinter import *
from tkinter import ttk
import tkinter as tk

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
    resultFrame = ttk.LabelFrame(tab2, text="Covid19 Application")
    resultFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

def City():
    resultFrame = ttk.LabelFrame(tab1, text="Covid19 Application")
    resultFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

    interactFrame = ttk.LabelFrame(tab1, text="Entry")
    interactFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=10)

    copyrightFrame = ttk.Frame(tab1)
    copyrightFrame.pack(fill=tk.X, expand=1, padx=10, pady=10)

    entry = ttk.Entry(interactFrame)
    entry.pack(side=LEFT, padx=10, pady=10)

    searchButton = ttk.Button(interactFrame, text="Search", style="Accent.TButton")
    searchButton.pack(side=LEFT,padx=10, pady=10)

    label = ttk.Label(copyrightFrame, text="Copyright 2020")
    label.pack(fill=tk.X, expand=1, padx=10, pady=10)

def App():
    Window()
    Global()
    City()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Covid19 Application")
    root.geometry("300x300")
    root.resizable(False, False)

    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "dark")

    App()

    root.mainloop()