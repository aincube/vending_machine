Coding Exercise - Vending Machine
===

Technical Requirements

* Backend : prefer C# (dotnet 6) otherwise written in Java, Python or Go ...
* UI of choice : Command-Line Interface (a.k.a. CLI), Web (Angular/React/Blazor or any framework), Desktop (UWP, Wpf) or Mobile (Xamarin, MAUI) ...
* Make use of design patterns and respect SOLID principles
* Unit Tests / Test-Driven Development (TDD)
* Test Coverage >= 85%

---

Vending Machine 
====================

In this exercise you will build the core software of a vending machine.  It will accept money, make change, maintain
inventory, and dispense products.  All the things that you might expect a vending machine to accomplish.

For simplicity no UI is required and all events will come via instructions entered by user via CLI i.e. "ENTER 1 or SELECT 12"
 
The point of this exercise is to make use of design patterns, SOLID principles and iterate over implementation using a TDD approach.

Features
========

Accept Coins
------------
  
_As a customer_  
_I want to insert coins_  
_So that I can pay for a selected product_  

The vending machine will accept valid coins (5cts to 2€) and reject invalid ones (1 and 2 cts).  When a
valid coin is inserted the amount of the coin will be added to the current amount, the current amount will be updated and visible to the user.
When there are no coins inserted, the machine displays INSERT COIN. 

* Command to accept coin : `ENTER <XXX>`
* Display current amount : `Amount entered: 0.55`

NOTE: We will assume all coins entered by user are in same currency than Vending machine. Cents are represented by two digits decimals i.e. 0.10 for 10cts.

Show Products
--------------
_As a customer_  
_I want to list available products_  
_So that I can select what I would like_  

Given there are three products identified by number: 1. cola for 1.00€, 2. chips for 0.50€, 3. candy for 0.65€.  
When sending the following command : `SHOW`
Then list of products with their prices and remaining stocks is displayed
```
COLA 1€ - 8 Item Left
Chips 0.50€ - 12 Items Left
Candy 0.65€ - SOLD OUT 
```

Select Product
--------------

_As a customer_  
_I want to select products_  
_So that I can choose which product I wish_  

Given there are three products identified by number: 1. cola for 1.00€, 2. chips for 0.50€, 3. candy for 0.65€.  
When sending the following command : `SELECT <NUMBER>`
Then provided that enough money has been inserted 
the product is dispensed (show a message)
and the change is returned if applicable 
and the machine displays THANK YOU.

If the user selects again, it will display INSERT COIN and the current amount will be set to 0.00€.  If there is not enough money inserted then the machine displays PRICE and the price of the item and subsequent checks of the display will display

Make Change
-----------

_As a customer_  
_I want to receive correct change_  
_So that I can retrieve amount of money which is over target price_  

When a product is selected (`SELECT <NUMBER>`) that costs less than the amount of money in the machine, then the remaining amount is placed
in the coin return.

Display a message before THANK YOU indicating returned money i.e. Please take your change: 0.10cts

Return Coins
------------

_As a customer_  
_I want to have my money returned_  
_So that I can change my mind about buying stuff from the vending machine_  

When the command `RETURN COINS`, the money the customer has placed in the machine is returned indicating returned money and the display shows INSERT COIN.

Sold Out
--------

_As a customer_  
_I want to be told when the item I have selected is not available_  
_So that I can select another item_  

When the item selected by the customer is out of stock, the machine displays SOLD OUT.  If the item selected is checked again,
it will display the amount of money remaining in the machine or INSERT COIN if there is no money in the machine.

NOTE: Default stock when machine is filled in is following
Product 1 - 15
Product 2 - 10
Product 3 - 20

Exact Change Only
-----------------

_As a customer_  
_I want to be told when exact change is required_  
_So that I can determine if I can buy something with the money I have before inserting it_  

When the machine is not able to make change with the money in the machine for any of the items that it sells, it will display EXACT CHANGE ONLY instead of INSERT COIN.
Machine needs to be initialize with a set of each coin types. As soon as machine is not able to return remaining cash it will display the message.
e.g. Machine has remaining 2 * 5cts, 1 * 10cts; User selects a product for 0.65€; User enters 1€ then EXACT CHANGE ONLY is displayed
e.g. Machine has remaining 2 * 5cts, 1 * 20cts; User selects a product for 0.75€; User enters 1€ then make change message is displayed; Machine has 5cts remaining

Nice-To-Have Requirements
========

Customizable
------------

Vending machine when started should ideally be customizable 

* indicating how many slots it can take, by default 3 (parameter like --slots 5).
* currency accepted, by default EUR (parameter like --currency EUR)
* definition of stocks per product (parameter like --stocks stockFile.csv)
    * Csv file with two columns ProductId;Stock i.e. 1;15 
* help to maintenance technician (parameters like --help)

Localizable
------------

Vending machine when can be change by user in different languages than English, Add German and French as potential options. 

Command from user could be `LANGUAGE <EN|DE|FR>`

All messages shown to user will be in this new selected language. For simplicity commands will stay as-is.



