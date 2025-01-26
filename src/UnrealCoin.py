import requests

def __init__(self, name, displayname, id, version, publisher):
  self.name         = name
  self.displayname  = displayname
  self.id           = id
  self.version      = version
  self.publisher    = publisher

  self_main = self
  return self_main

def coin_prices():

  doritocoin = 'https://raw.githubusercontent.com/adaves1/UnrealCoin/master/src/api/coinprices/doritocoin.txt'
  doritocoin_r = requests.get(doritocoin)

  if doritocoin_r.status_code == 200:
    print(f"DoritoCoin: {doritocoin_r}")
  else:
    print(f"Failed to retrieve the coin price. Status code: {doritocoin_r.status_code}")

def coin_price(coin):
  if coin == "doritocoin":
    doritocoin = 'https://raw.githubusercontent.com/adaves1/UnrealCoin/master/src/api/coinprices/doritocoin.txt'
    doritocoin_r = requests.get(doritocoin)

    if doritocoin_r.status_code == 200:
      print(f"DoritoCoin: {doritocoin_r}")
    else:
      print(f"Failed to retrieve the coin price. Status code: {doritocoin_r.status_code}")
  else:
    return "The DoritoCoin Price is not available. Try again later."
