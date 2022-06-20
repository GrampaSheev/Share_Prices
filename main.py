import requests
import yfinance as yf

Y = "Y"
N = "N"

#What share and has shares
share = yf.Ticker(input("What share would you like?(Enter the Ticker/Stock Symbol ex: msft or appl)"))
HaveShares = input("Do you have any shares? Y/N")

#Currencies options
OutputCurrency = input("Choose currency to convert too. Choises are USD/GBP/EUR/JPY/AUD/CAD/CHF/CNY/SEK/NZD")

#Ticker and Exchange rates
amount = share.info["currentPrice"]
url = f"https://api.apilayer.com/exchangerates_data/convert?to={OutputCurrency}&from=USD&amount={amount}"

#Currencies
USD = "$"
GBP = "£"
EUR = "€"
JPY = "¥"
AUD = "$"
CAD = "$"
CHF = "CHf"
CNY = "¥"
SEK = "Kr"
NZD ="$"

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

if data == {'error': {'code': 'invalid_from_currency', 'message': 'You have entered an invalid "from" property. [Example: from=EUR]'}}:
  print("Invalid Currency")


else:
  # Owned
  if HaveShares.lower() == Y.lower():
    SharesNum = float(input("Enter numner of shares"))
    AssetsOwned = SharesNum * data["result"]
    print(OutputCurrency, AssetsOwned)

  # Unowned
  if HaveShares.lower() == N.lower():
    print(OutputCurrency, data["result"])
