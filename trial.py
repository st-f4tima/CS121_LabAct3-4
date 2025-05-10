# Baka may pwede kayong idagdag na specialized properties per subclass. 
# Then baka gusto nyo rin gawing responsive, dagdagan or ayusin nyo nalang...

from abc import ABC, abstractmethod
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

exchange_rates = {
    'PHP': 0.018,
    'JPY': 0.0069,
    'USD': 1.0,
    'INR': 0.012
}

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

    def __str__(self):
        return (
            f'\n────💵 Currency Information 💵────\n\n'
            f"Currency: {self.currency_code} ({self.symbol})\n"
            f"Subunit: {self.sub_unit}\n"
            f"Exchange Rate to USD: {self._rate_to_usd}"
        )

class PhilippinePeso(Currency):
    def __init__(self):
        super().__init__("PHP", "₱", "Centavos", exchange_rates['PHP'])

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

class JapaneseYen(Currency):
    def __init__(self):
        super().__init__("JPY", "¥", "Sen", exchange_rates['JPY'])

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

class USDollar(Currency):
    def __init__(self):
        super().__init__("USD", "$", "Cent", exchange_rates['USD'])

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

class IndianRupee(Currency):
    def __init__(self):
        super().__init__("INR", "₹", "Paise", exchange_rates['INR'])

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

def get_currency_instance(currency_code):
    if currency_code == "PHP":
        return PhilippinePeso()
    elif currency_code == "JPY":
        return JapaneseYen()
    elif currency_code == "USD":
        return USDollar()
    elif currency_code == "INR":
        return IndianRupee()
    else:
        raise ValueError(f"Unsupported currency.")

def main():
    while True:
        print("\n─────────────🌐 Currency Converter 🌐─────────────\n")
        print("Choose an option:")
        print("1. Convert to one currency")
        print("2. Convert to many currencies")
        print("3. See which currency is stronger")
        print("4. View exchange rates")
        print("5. Quit")
        try:
            choice = input('Enter your choice (1-5): ').strip()

            if choice == "1":
                amount = float(input('\nEnter amount: '))
                base_currency_code = input('Enter base currency code (PHP, JPY, USD, INR): ').strip().upper()
                currency = get_currency_instance(base_currency_code)
                target_currency_code = input('Enter target currency code (PHP, JPY, USD, INR): ').strip().upper()
                if target_currency_code not in exchange_rates:
                    raise ValueError(f"Unsupported currency.")
                result = currency.convert_to(amount, target_currency_code)

                clear_screen()
                print(currency)
                print("\n💱 Conversion Results:")
                print(f"{amount:,.2f} {base_currency_code} = {result:,.2f} {target_currency_code}\n")
            
            elif choice == "2":
                amount = float(input('\nEnter amount: '))
                base_currency_code = input('Enter base currency code (PHP, JPY, USD, INR): ').strip().upper()
                currency = get_currency_instance(base_currency_code)
                clear_screen()
                print(currency)
                print(f"\n📊 Converting to all other currencies:")
                for code in exchange_rates:
                    if code != base_currency_code:
                        result = currency.convert_to(amount, code)
                        print(f"{amount:,.2f} {base_currency_code} = {result:,.2f} {code}")
                print()

            #choice 3
            #choice 4
            #choice 5
            
            else:
                raise ValueError('Invalid option. Please choose a number between 1 and 5.')

            print('───────────────────────────────────')
            response = input('Do you want to ask again (n/y)? ').strip().lower()
            if response != 'y':
                print('\nThank you!')
                break
            else:
                clear_screen()
            
        except ValueError as e:
            print(f'\nError: {e}')
            input('Please press enter to continue...')
            clear_screen()

if __name__ == "__main__":
    main()
