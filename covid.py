# def getData():
#     global data
#     url = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true"
#     response = requests.get(url)
#     data = response.json()

# def printData():
#     print("Total Cases: " + '{:,.0f}'.format(data['infected'])) 
#     print("Total Death: " + '{:,.0f}'.format(data['died']))
#     print("Total Recovered: " + '{:,.0f}'.format(data['recovered']))
#     print("Total Active: " + '{:,.0f}'.format(data['infected'] - data['died'] - data['recovered']))
#     print("----------------------------------------------------")

# def exportData():
#     city = input("Enter a city: ")
#     url = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true"
#     response = requests.get(url)
#     data = response.json()
#     for i in data['locations']:
#         if i['name'] == city:
#             print("Name: " + i['name'])
#             print("Cases Today: " + '{:,.0f}'.format(i['casesToday'])) 
#             print("Death Today: " + '{:,.0f}'.format(i['death']))
#             print("Recovered Today: " + '{:,.0f}'.format(i['recovered']))
#         else :
#             print("No city data")
# def getCityData():
#     #loop if the answer is not 1 or 2
#     choice = input("Checking for city data?\n1. Yes\n2. No\n")
#     if choice == "1":
#         exportData()
#     elif choice == "2":
#         print("No city data")

# if __name__ == "__main__":
#     getData()
#     printData()
#     getCityData()


from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.font import BOLD
import requests

NAME = "PC Covid"
DEFAULTCITY = "Hà Nội"

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
    seperator.pack(fill=tk.X, padx=10, pady=10)

    globalData = ttk.Label(resultFrameGlobal, text=
    "Total Cases: " + '{:,.0f}'.format(data['infected']) + "\n"+  
    "Total Death: " + '{:,.0f}'.format(data['died']) + "\n" +
    "Total Recovered: " + '{:,.0f}'.format(data['recovered']) + "\n" +
    "Total Active: " + '{:,.0f}'.format(data['infected'] - data['died'] - data['recovered']) + "\n")
    globalData.pack(padx=10, pady=3)

    globalData2 = ttk.Label(resultFrameGlobal, text=
    "Cases Today: " + '{:,.0f}'.format(data['infectedToday']) + "\n"+  
    "Death Today: " + '{:,.0f}'.format(data['diedToday']) + "\n" 
    "Recovered Today: " + '{:,.0f}'.format(data['recoveredToday']))
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

    searchButton = ttk.Button(interactFrame, text="Search", style="Accent.TButton", command=getDataFromCity)
    searchButton.pack(side=LEFT,padx=10, pady=10)

    label = ttk.Label(copyrightFrame, text="Copyright © 2021 by Khoa Nguyen")
    label.pack(padx=10, pady=10, side=BOTTOM)
    DataCity()

def DataCity():
    global cityTitle, cityData2
    city = "Hà Nội"
    cityTitle = ttk.Label(resultFrame, text= city + " Covid19 Information", font=("Arial", 13, BOLD))
    cityTitle.pack(side=TOP, padx=10, pady=(10,0))

    seperator = ttk.Separator(resultFrame, orient=tk.HORIZONTAL)
    seperator.pack(fill=tk.X, padx=10, pady=10)

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
            cityTitle.config(text=i['name'] + " Covid19 Information")
            cityData2.config(text="Cases Today: " + '{:,.0f}'.format(i['casesToday']) + "\n" +
            "Recovered Today: " + '{:,.0f}'.format(i['recovered']) + "\n" +
            "Total Death: " + '{:,.0f}'.format(i['death']))

def getDataFromCity():
    city = entry.get()
    url = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true"
    response = requests.get(url)
    data = response.json()
    for i in data['locations']:
        if i['name'] == city:
            cityTitle.config(text=i['name'] + " Covid19 Information")
            cityData2.config(text="Cases Today: " + '{:,.0f}'.format(i['casesToday']) + "\n" +
            "Recovered Today: " + '{:,.0f}'.format(i['recovered']) + "\n" +
            "Total Death: " + '{:,.0f}'.format(i['death']))

def App():
    API()
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