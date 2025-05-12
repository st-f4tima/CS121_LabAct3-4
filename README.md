![Currency logo](currency(1).jpg)

#  1204: A Conversion Story
### An Object-Oriented Programming Project: Class 💸Currency💸
> *Because not all heroes has every cash. We don't know how to make cents of it all but we'll try...* Your reliable, no-nonsense **currency converter** will save you from bad math exchange rate and worse😩. We're making international transactions a little less tragic - one line of code at a time. 

**Project 1204: A Conversion Story** runs in the world of Python OOP, where clean structure, solid principle, and reusable logic rule the economy. Whether you're dealing in Dollars, Peso, Rupee, or Yen, this converter has your back. 

This project consists of an abstract base class `Currency` that defines a standard interface for all currencies - the parent class. It is extended by four subclasses namely: `PhilippinePeso`, `JapaneseYen`, `USDollar`, and `IndianRupee`. Each currency class comes with the following properties inherited from `Currency`:

- `amount`: a private property that signifies the value of each currency
- `currency_code`: code representation (ex. "PHP", "JPY", "USD", "INR")
- `symbol`: currency symbol (ex. "₱", "¥", "$", "₹")
- `sub_unit`: fractional unit (ex. "centavo", "sen")
- `rate_to_usd`: the exchange rate relative to 1 USD

And also the method:

- `convert_to(amount, target_currency)`: converts the current amount into a specified target currency using USDollar as a base.
- `compare_with(amount, other_currency)`: compares which in two different currencies is stronger using USDollar as basis currency.
