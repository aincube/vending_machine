from enum import Enum

class Currencies(Enum):
  EUR = '€'
  USD = '$'

class VM():
  def __init__(self, 
              slots: int = 3, 
              currency: Currencies = Currencies.EUR, 
              acceptedCoins: tuple = (),
              productsList: dict = {},
              productsStock: dict = {},
              changeStock: dict = {}
              ) -> None:
    self.slots: int = slots
    self.currency: Currencies = currency
    self.state: str = None        
    self.displayText: str = 'INSERT COIN' # TODO: Change to message from i18n
    self.selectedItem: int|None = None
    self.amount: float = 0.0
    self.coinReturn: float = 0.0
    self.acceptedCoins: tuple = acceptedCoins
    self.productsList: dict = productsList
    self.productsStock: dict = productsStock
    self.changeStock: dict = changeStock

  def insertCoin(self, coin: str) -> float|None:
    if float(coin) in self.acceptedCoins:
      self.amount += float(coin)
      return self.amount
    else:
      # TODO: Throw an error or implement a reject machanism
      return None
  
  def returnCoins(self) -> float:
    returnedAmount = self.amount
    self.amount = 0.0
    self.coinReturn = returnedAmount
    return returnedAmount

  def getStocks(self):
    return self.productsStock

  def dispenseProduct(self, pID: int) -> int:
    updatedStockValue = self.productsStock[pID] - 1
    self.productsStock[pID] = updatedStockValue
    self.displayText = 'Please take your {0}'.format(self.productsList[pID]['name'])
    return updatedStockValue


  def getStocksString(self) -> str:
    productsList = ''
    for pkey, pvalue in self.productsStock.items():      
      curProduct = self.productsList[pkey]      
      ending = '{4} Items Left' if pvalue > 0 else 'SOLD OUT' # TODO: Change to message from i18n
      fstring = '{0}. {1} {2:.2f}{3} - ' + ending + '\n'
      productsList += fstring.format(pkey, curProduct['name'], curProduct['price'], self.currency.value, pvalue)
    return productsList

  def selectItem(self, ItemID: str):
    try:
      pID = int(ItemID)
    except Exception as e:
      # TODO: Not an integer pid
      pass
    self.selectedItem = pID
    product = self.productsList[pID]
    productPrice = product['price']
    if product is not None:
      if self.amount == productPrice:
        self.amount = 0
        self.dispenseProduct(pID)
        self.displayText = 'THANK YOU' # TODO: Change to message from i18n
      elif self.amount > productPrice:
        changeCoins = self.coinsForChange(
          allowedCoins = self.acceptedCoins, 
          amount = self.amount, 
          price = productPrice)
        exactChange = self.isExactChange(allowedCoins = self.acceptedCoins, stock = self.changeStock, coins = changeCoins)
        if not exactChange:
          self.amount = self.amount - productPrice
          returned = self.returnCoins()
          self.displayText = 'Please take your change: {0:.2f}{1}'.format(returned, self.currency.value) # TODO: Change to message from i18n
          self.dispenseProduct(pID)
        else:
          self.displayText = 'EXACT CHANGE ONLY' # TODO: Change to message from i18n
      else:
        self.displayText = 'PRICE {0}'.format(productPrice)
        
  def getSelectedItem(self) -> int|None:
    return self.selectedItem

  def getAmount(self) -> float:
    return self.amount
  
  def getAmountString(self) -> str:
    return "{0:.2f} {1}".format(self.getAmount(), self.currency.value)

  def coinsForChange(self, allowedCoins: tuple, amount: float, price: float) -> dict:
    """
    Generate list of coins for a given amount and price

    :param allowedCoins: tuple of floats with allowed coins
    :param amount: how much user inserted
    :param price: price of the product
    :returns: dictionary with list of coins and number of coins needed to give a change
    """
    result = {}
    change = amount - price
    if change > 0:
      rest = change
      for coin in tuple(sorted(allowedCoins, reverse=True)):      
        result[f'{coin:.2f}'] = rest // coin
        rest = round(rest % coin, 2)
    return result

  def isExactChange(self, allowedCoins: tuple, stock: dict, coins: dict) -> bool:
    """
    Check if we in Exact Change mode

    :param allowedCoins: tuple of floats with allowed coins
    :param stock: dict with our stock of the coins
    :param coins: dict with coins and number of coins needed for the change
    :returns: True if we are in Exact Change mode
    """
    for coin in allowedCoins:
      if stock[f'{coin:.2f}'] < coins[f'{coin:.2f}']:
        return True
    return False
