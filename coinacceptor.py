from typing import Literal, get_args

AllowedCoins = Literal['0.05', '0.10', '0.20', '0.50', '1.0', '2.0']

class CoinAcceptor():
  def __init__(self, acceptedCoins: Literal = AllowedCoins):
    self.acceptedCoins: tuple = get_args(acceptedCoins)
    self.amount: float = 0.0
  
  def insertCoin(self, coin: str) -> float|None:
    if coin in self.acceptedCoins:
      self.amount += float(coin)
      return self.amount
    else:
      # TODO: Throw an error or implement a reject machanism
      return None
  
  def getAmount(self):
    return self.amount

ca = CoinAcceptor(AllowedCoins)
ca.insertCoin('0.05')
ca.insertCoin('0.02')
ca.insertCoin('0.10')
ca.insertCoin('1.0')
print("{:.2f}".format(ca.getAmount()))