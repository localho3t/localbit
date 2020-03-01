import requests
import time
print("Bitcoin\n")
while(True):
      re = requests.get("https://api.livecoin.net/exchange/ticker?currencyPair=BTC/USD")
      bit = re.json()
      print("Latest Price Today : " , bit['last']," BIT")
      time.sleep(600)


