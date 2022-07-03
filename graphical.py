import requests
import yfinance as yf
import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Shares Viewer")
window.geometry("300x150")

def ShowResults():
    global data
    # setup
    # Ticker and Exchange rates
    share = yf.Ticker(TkShare.get())
    amount = share.info["currentPrice"]
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={Currency.get()}&from=USD&amount={amount}"

    # Auth
    payload = {}
    headers = {
        "apikey": "SylZpkQ5hnB3Dovy5adcj5OukR9hOEFV"
    }

    # API request
    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.text
    data = response.json()
    if HaveSharesOn.get() == 0:
        assets = data["result"]

    else:
        assets = data["result"] * int(HowManyShares.get())


    money = round(assets,2)
    total =Currency.get(),money
    sharePrice = Label(window, text=total )
    sharePrice.grid(row=6, column=0)

def HowMany():
    global HowManyShares
    HowManyLabel = Label(window, text = "How many?")
    HowManyLabel.grid(row=3,column=1)
    HowManyShares = Entry(window, width=10)
    HowManyShares.grid(row=3, column=2)

#Do you have shares
HaveSharesOn = IntVar()

HaveShares =Checkbutton(window, text="Do you have shares?", variable=HaveSharesOn, command=HowMany)
HaveShares.deselect()
HaveShares.grid(row=3, column=0)


#Ticker Shares
TkShareLabel = Label(window, text="Enter Ticker/Short Name")
TkShare = Entry(window, width=10)

TkShareLabel.grid(row=1, column=0)
TkShare.grid(row=1,column=1)

#Currency select

CurrencyLabel = Label(window, text = "Choose a currency")
CurrencyLabel.grid(row=4,column=0)
Currency = StringVar()
Currency.set("USD")
CurrencySelect = OptionMenu(window, Currency, "USD","GBP", "EUR", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD")
CurrencySelect.grid(row=4,column=1)



Results = Button(window, text = "Share Price Amout", command=ShowResults)
Results.grid(row=5, column=0)

window.mainloop()
