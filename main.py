import requests
import yfinance as yf

Y = "Y"
N = "N"

share = yf.Ticker(input("What share would you like?(Enter the Ticker/Stock Symbol ex: msft or appl)"))
HaveShares = input("Do you have any shares? Y/N")

amount = share.info["currentPrice"]
url = f"https://api.apilayer.com/exchangerates_data/convert?to=GBP&from=USD&amount={amount}"

payload = {}
headers= {
  "apikey": "SylZpkQ5hnB3Dovy5adcj5OukR9hOEFV"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
data = response.json()

if HaveShares.lower() == Y.lower():
  SharesNum = float(input("Enter numner of shares"))
  


if HaveShares.lower() == N.lower():
  print(data["result"])
