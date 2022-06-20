import requests
import yfinance as yf

Y = "Y"
N = "N"

#What share and has shares
share = yf.Ticker(input("What share would you like?(Enter the Ticker/Stock Symbol ex: msft or appl)"))
HaveShares = input("Do you have any shares? Y/N")

#Currencies options
to = input("Choose currency to convert too. Choises are USD/GBP/EUR")
from = input("Choose currency to convert from. Choises are USD/GBP/EUR")

#Ticker and Exchange rates
amount = share.info["currentPrice"]
url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

#Currencies
USD = "$"
GBP = "£"
EUR = "€"

#Auth
payload = {}
headers= {
  "apikey": "SylZpkQ5hnB3Dovy5adcj5OukR9hOEFV"
}

#API request
response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
data = response.json()


#Owned
if HaveShares.lower() == Y.lower():
  SharesNum = float(input("Enter numner of shares"))
  AssetsOwned = SharesNum * data["result"] 
  print(to, AssetsOwned) 
  

#Unowned
if HaveShares.lower() == N.lower():
  print(to, data["result"])
