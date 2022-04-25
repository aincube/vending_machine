from vm import VM, Currencies

AllowedCoins = (2.00, 1.00, 0.50, 0.20, 0.10, 0.05)
AllowedCommands = ('ENTER', 'SHOW', 'SELECT', 'RETURN', 'LANGUAGE')
Languages = ('EN', 'DE', 'FR')
InitialStock = {
  1: 15,
  2: 10,
  3: 20,
  4: 0
}

# TODO: What if the price will be 0.67 and 1%2 cents are not allowed?
ProductsList = {
  1: { 'name': 'COLA', 'price': 1.0 },
  2: { 'name': 'Chips', 'price': 0.5 },
  3: { 'name': 'Candy', 'price': 0.65 },
  4: { 'name': 'Pepsi', 'price': 1.1 }
}

# TODO: ? Fill with func from AllowedCoins
changeStock = {
  '0.05' : 2, 
  '0.10' : 1, 
  '0.20' : 1, 
  '0.50' : 0, 
  '1.00' : 0, 
  '2.00' : 0
}

if __name__ == "__main__":
  fstring = '[ SP: {selectedItem} ] [ AMOUNT: {amount} ] [ CR: {coinReturn} ] [ {displayMessage} ] Type command: '
  vm = VM(acceptedCoins = AllowedCoins, 
          productsList = ProductsList,
          productsStock = InitialStock,
          changeStock = changeStock)

  while True:
    try:
      userinput = input(fstring.format(
        amount = vm.getAmountString(), 
        selectedItem = vm.selectedItem, 
        displayMessage = vm.displayText,
        coinReturn = vm.coinReturn
        )).strip().split(' ')
      command = userinput[0].upper()
      try:
        param = userinput[1]
      except IndexError:
        pass
      if command in AllowedCommands:
        match command:
          case 'SHOW':
            print(vm.getStocksString())
          case 'ENTER':
            vm.insertCoin(param)
          case 'SELECT':
            vm.selectItem(param)
          case 'RETURN':
            vm.returnCoins()
          case _:
            pass
      else:
        # TODO: Implement "Wrong command" message
        pass
    except Exception as e:
      print(e)