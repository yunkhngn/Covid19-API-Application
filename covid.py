import requests

def getData():
    global data
    url = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true"
    response = requests.get(url)
    data = response.json()

def printData():
    print("Total Cases: " + '{:,.0f}'.format(data['infected'])) 
    print("Total Death: " + '{:,.0f}'.format(data['died']))
    print("Total Recovered: " + '{:,.0f}'.format(data['recovered']))
    print("Total Active: " + '{:,.0f}'.format(data['infected'] - data['died'] - data['recovered']))
    print("----------------------------------------------------")

def exportData():
    city = input("Enter a city: ")
    url = "https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true"
    response = requests.get(url)
    data = response.json()
    for i in data['locations']:
        if i['name'] == city:
            print("Name: " + i['name'])
            print("Cases Today: " + '{:,.0f}'.format(i['casesToday'])) 
            print("Death Today: " + '{:,.0f}'.format(i['death']))
            print("Recovered Today: " + '{:,.0f}'.format(i['recovered']))
        else :
            print("No city data")
def getCityData():
    #loop if the answer is not 1 or 2
    choice = input("Checking for city data?\n1. Yes\n2. No\n")
    if choice == "1":
        exportData()
    elif choice == "2":
        print("No city data")

if __name__ == "__main__":
    getData()
    printData()
    getCityData()
