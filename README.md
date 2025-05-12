# CS 121 Laboratory Activity 3
![Currency logo](currency(1).jpg)

<h3 align="center">
  <a href="#📦-features">Features</a> •
  <a href="#🏗️-how-it-works">How It Works</a> •
  <a href="#🧠-tech-stack">Tech Stack</a> •
  <a href="#👥-authors">Authors</a> •
</h3>

<h1 align="center">
 💵THE CONVERSION STORY💵
</h1>

### An Object-Oriented Programming Project: Class 💸Currency💸

> *Because not all heroes has every cash. We don't know how to make cents of it all but we'll try...* Your reliable, no-nonsense **currency converter** will save you from bad math exchange rate and worse😩. We're making international transactions a little less tragic - one line of code at a time. 

**Project 1204: A Conversion Story** runs in the world of Python OOP, where clean structure, solid principle, and reusable logic rule the economy. Whether you're dealing in Dollars, Peso, Rupee, or Yen, this converter has your back. 


## 📦 Features

- Convert a specific amount from one currency to another
- Convert a single currency to multiple other currencies
- Compare the relative strength of two currencies
- Display current hardcoded exchange rates
- Clean command-line UI with menus
- Currency metadata including symbols, subunits, and       central banks



## 🏗️ How It Works

This project consists of an abstract base class `Currency` that defines a standard interface for all currencies - the parent class.

```python
class Currency(ABC):
    def __init__(self, currency_code, symbol, sub_unit, rate_to_usd):
        self.currency_code = currency_code
        self.symbol = symbol
        self.sub_unit = sub_unit
        self.__amount = 0.0
        self._rate_to_usd = rate_to_usd
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount

    @abstractmethod
    def convert_to(self, amount, target_currency_code):
        pass

    def compare_with(self, amount, other_currency):
        self_usd = self.convert_to(amount, "USD")
        other_usd = other_currency.conver_to(amount, "USD")

        if self_usd > other_usd:
            reutrn 1
        elif self_usd < other_usd:
            return -1
        else:
            return 0
            
    def __str__(self):
        return (
            f'\n─────────────💵 Currency Information 💵─────────────\n\n'
            f"Currency: {self.currency_code} ({self.symbol})\n"
            f"Subunit: {self.sub_unit}\n"
            f"Exchange Rate to USD: {self._rate_to_usd}"
        )
```
It is extended by four subclasses namely: `PhilippinePeso`, `JapaneseYen`, `USDollar`, and `IndianRupee`. Each currency class comes with the following properties inherited from `Currency`:

- `amount`: a private property that signifies the value of each currency
- `currency_code`: code representation (ex. "PHP", "JPY", "USD", "INR")
- `symbol`: currency symbol (ex. "₱", "¥", "$", "₹")
- `sub_unit`: fractional unit (ex. "centavo", "sen")
- `rate_to_usd`: the exchange rate relative to 1 USD

And also the method:

- `convert_to(amount, target_currency)`: converts the current amount into a specified target currency using USDollar as a base.

- `compare_with(amount, other_currency)`: compares which in two different currencies is stronger using USDollar as basis currency.
Conversions work by converting first to USD, then from USD to the target currency.


## 🧠 Tech Stack

- `Python` for programming language
- `abc` for abstract base classes
- `os` for cross-platform terminal clearing


## 👥 Authors
- Fatima Pura
- Nikki Limboc
- Gian Louie Baes
- Lance Kert Mendoza

## 🚀 Usage


