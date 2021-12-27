from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import requests


NAME = "PC Covid"
DEFAULTCITY = "Hà Nội"
THEME = "light"
LANGUAGE = "English"

def Window():
    global tab1, tab2, tab3
    bigframe = ttk.Frame(root)
    bigframe.pack(fill=tk.BOTH, expand=1)

    notebook = ttk.Notebook(bigframe)
    notebook.pack(fill=tk.BOTH, expand=1)

    tab1 = ttk.Frame(notebook)
    notebook.add(tab1, text="Total")

    tab2 = ttk.Frame(notebook)
    notebook.add(tab2, text="City")

    tab3 = ttk.Frame(notebook)
    notebook.add(tab3, text="About")

def API():
    global data
    url = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true"
    response = requests.get(url)
    data = response.json()

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
    seperator.pack(fill=tk.X, padx=10, pady=5)

    globalData = ttk.Label(resultFrameGlobal, text=
    "Total Cases: " + '{:,.0f}'.format(data['infected']) + "\n"+  
    "Total Death: " + '{:,.0f}'.format(data['died']) + "\n" +
    "Total Recovered: " + '{:,.0f}'.format(data['recovered']) + "\n" +
    "Total Active: " + '{:,.0f}'.format(data['infected'] - data['died'] - data['recovered']) + "\n")
    globalData.pack(padx=10, pady=(3,0))

    seperator = ttk.Separator(resultFrameGlobal, orient=tk.HORIZONTAL)
    seperator.pack(fill=tk.X, padx=10, pady=0)

    globalData2 = ttk.Label(resultFrameGlobal, text=
    "Cases Today: " + '{:,.0f}'.format(data['infectedToday']) + "\n"+  
    "Death Today: " + '{:,.0f}'.format(data['diedToday']) + "\n" 
    "Recovered Today: " + '{:,.0f}'.format(data['recoveredToday']))
    globalData2.pack(padx=10, pady=3)

def City():
    global resultFrame, entry, searchButton
    resultFrame = ttk.LabelFrame(tab2, text="Covid19 Information")
    resultFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=(10,0))

    interactFrame = ttk.LabelFrame(tab2, text="Entry")
    interactFrame.pack(fill=tk.BOTH, expand=1, padx=10, pady=0)

    copyrightFrame = ttk.Frame(tab2)
    copyrightFrame.pack(fill=tk.X, expand=1, padx=10, pady=0)

    entry = ttk.Entry(interactFrame)
    entry.pack(side=LEFT, padx=10, pady=3)

    searchButton = ttk.Button(interactFrame, text="Search", style="Accent.TButton", command=getDataFromCity)
    searchButton.pack(side=LEFT,padx=10, pady=10)

    label = ttk.Label(copyrightFrame, text="Copyright © 2021 by Khoa Nguyen")
    label.pack(padx=10, pady=10, side=BOTTOM)
    DataCity()

def DataCity():
    global cityTitle, cityData2
    city = "Hà Nội"
    cityTitle = ttk.Label(resultFrame, text= city + " Information", font=("Arial", 13, BOLD))
    cityTitle.pack(side=TOP, padx=10, pady=(10,0))

    seperator = ttk.Separator(resultFrame, orient=tk.HORIZONTAL)
    seperator.pack(fill=tk.X, padx=10, pady=5)

    cityData2 = ttk.Label(resultFrame, text=
    "Cases Today: " + "\n" + 
    "Recovered Today: " + "\n" +
    "Total Death: ")
    cityData2.pack(padx=10, pady=10)
    defaultCityGet()

def defaultCityGet():
    global city
    city = DEFAULTCITY
    for i in data['locations']:
        if i['name'] == city:
            cityTitle.config(text=i['name'] + " Information")
            cityData2.config(text="Cases Today: " + '{:,.0f}'.format(i['casesToday']) + "\n" +
            "Recovered Today: " + '{:,.0f}'.format(i['recovered']) + "\n" +
            "Total Death: " + '{:,.0f}'.format(i['death']))

def getDataFromCity():
    city = entry.get().lower()
    lst = [word[0].upper() + word[1:] for word in city.split()]
    city = " ".join(lst)

    if city == "Tp. Hồ Chí Minh" or city == "Hồ Chí Minh":
        city = "TP. Hồ Chí Minh"
        print(city)
    if city == "Bà Rịa" or city == "Bà Rịa Vũng Tàu" or city == "Vũng Tàu" or city == "Bà Rịa - Vũng Tàu":
        city = "Bà Rịa – Vũng Tàu"
        print(city)

    for i in data['locations']:
        if i['name'] == city:
            cityTitle.config(text=i['name'] + " Information")
            cityData2.config(text="Cases Today: " + '{:,.0f}'.format(i['casesToday']) + "\n" +
            "Recovered Today: " + '{:,.0f}'.format(i['recovered']) + "\n" +
            "Total Death: " + '{:,.0f}'.format(i['death']))
            entry.state(["!invalid"])
            break
        else:
            entry.state(["invalid"])

def About():
    global LanguageCurrent
    Title = ttk.Label(tab3, text="About", font=("Arial", 13, BOLD))
    Title.pack(side=TOP, padx=10, pady=(10,0))

    seperator = ttk.Separator(tab3, orient=tk.HORIZONTAL)
    seperator.pack(fill=tk.X, padx=10, pady=5)

    content = ttk.Label(tab3, text=NAME + " is created by Khoa Nguyen.\n\n"
    "This app is a project of the course of Software Engineering at the University. Feel free to get the open source but please remain the copyrighted information. If you have any information, please contact me or submit it into Github!\n", wraplength= 270, justify=LEFT)
    content.pack(padx=10, pady=0)

    #create a redicted link to Github that clickable
    Language = ttk.LabelFrame(tab3, text="Language")
    Language.pack(side=TOP, padx=10, pady=5, fill=tk.X)

    LanguageButton = ttk.Button(Language, text="Language")
    LanguageButton.pack(side=LEFT, padx=10, pady=10)

    LanguageCurrent = ttk.Label(Language, text=LANGUAGE)
    LanguageCurrent.pack(side=RIGHT, padx=10, pady=10)

    Copyright = ttk.Label(tab3, text="Copyright © 2021 by Khoa Nguyen")
    Copyright.pack(padx=10, pady=10, side=BOTTOM)

def App():
    API()
    Window()
    Global()
    City()
    About()

if __name__ == "__main__":
    root = tk.Tk()
    root.title(NAME)
    root.geometry("300x330")
    root.resizable(False, False)

    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", THEME)

    App()

    root.mainloop()