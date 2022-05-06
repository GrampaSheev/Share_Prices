import yfinance as yf
import time

AMD = yf.Ticker('AMD')

s = "s"
u = "u"
UorS=input("U or S ")


if UorS.lower() == u.lower():
  while True:
        shareprice_G = AMD.info['currentPrice']
        shareprice = round(shareprice_G * 0.81)
        print(shareprice)
        time.sleep(1)

elif UorS.lower()==s.lower():
    while True:
        shareprice_G = AMD.info['currentPrice']
        shareprice = round(shareprice_G * 0.81)
        mymon = round(shareprice * 2.899014,2)
        print(mymon)
        time.sleep(1)
