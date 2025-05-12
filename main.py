from abc import ABC, abstractmethod
import os

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
            f'\n─────────────💵 Currency Information 💵─────────────\n\n'
            f"Currency: {self.currency_code} ({self.symbol})\n"
            f"Subunit: {self.sub_unit}\n"
            f"Exchange Rate to USD: {self._rate_to_usd}"
        )

class PhilippinePeso(Currency):
    def __init__(self):
        super().__init__("PHP", "₱", "Centavos", exchange_rates['PHP'])
        self.central_bank = "Bangko Sentral ng Pilipinas"

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nCentral Bank: {self.central_bank}"

class JapaneseYen(Currency):
    def __init__(self):
        super().__init__("JPY", "¥", "Sen", exchange_rates['JPY'])
        self.central_bank = "Bank of Japan"

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nCentral Bank: {self.central_bank}"

class USDollar(Currency):
    def __init__(self):
        super().__init__("USD", "$", "Cent", exchange_rates['USD'])
        self.central_bank = "Federal Reserve"

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nCentral Bank: {self.central_bank}"

class IndianRupee(Currency):
    def __init__(self):
        super().__init__("INR", "₹", "Paise", exchange_rates['INR'])
        self.central_bank = "Bank of India"

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

    def __str__(self):
        base_info = super().__str__()
        return f"{base_info}\nCentral Bank: {self.central_bank}"

# Functions

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n─────────────🌐 Currency Converter 🌐─────────────\n")
    print("Choose an option:")
    print("1. Convert to one currency")
    print("2. Convert to many currencies")
    print("3. See which currency is stronger")
    print("4. View exchange rates")
    print("5. About")
    print("6. Quit")
        
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
        display_menu()
        try:
            choice = input('Enter your choice (1-6): ').strip()

            if choice == "1":
                try: 
                    amount = float(input('\nEnter amount: '))
                    
                    base_currency_code = input('Enter base currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if base_currency_code not in exchange_rates:
                        raise Exception(f"Unsupported currency.")

                    target_currency_code = input('Enter target currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if target_currency_code not in exchange_rates:
                        raise Exception(f"Unsupported currency.")

                    currency = get_currency_instance(base_currency_code)
                    result = currency.convert_to(amount, target_currency_code)

                    clear_screen()
                    print(currency)
                    print("\n💱 Conversion Results:")
                    print(f"{amount:,.2f} {base_currency_code} = {result:,.2f} {target_currency_code}")
                
                except ValueError:
                    print('Error: Invalid input. Please enter a valid number for the amount.')
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "2":
                try: 
                    amount = float(input('\nEnter amount: '))
                    base_currency_code = input('Enter base currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if base_currency_code not in exchange_rates:
                        raise Exception(f"Unsupported currency.")
                    
                    currency = get_currency_instance(base_currency_code)
                    clear_screen()
                    print(currency)
                    print(f"\n📊 Converting to all other currencies:")
                    for code in exchange_rates:
                        if code != base_currency_code:
                            result = currency.convert_to(amount, code)
                            print(f"{amount:,.2f} {base_currency_code} = {result:,.2f} {code}")
                
                except ValueError:
                    print('Error: Invalid input. Please enter a valid number.')
                except Exception as e:
                    print(f"Error: {e}")


            elif choice == "3":
                try:
                    amount = float(input('\nEnter amount to compare: '))
                    currency1 = input('Enter first currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if currency1 not in exchange_rates:
                        raise Exception(f"Unsupported currency.")

                    currency2 = input('Enter second currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if currency2 not in exchange_rates:
                        raise Exception(f"Unsupported currency.")

                    currency1_obj = get_currency_instance(currency1)
                    currency2_obj = get_currency_instance(currency2)

                    usd_value1 = currency1_obj.convert_to(amount, "USD")
                    usd_value2 = currency2_obj.convert_to(amount, "USD")

                    clear_screen()
                    print(f"\n─────────────💵 Currency Comparison 💵─────────────")
                    print(f"\nComparing {currency1} and {currency2} (converted to USD):")
                    print(f"{amount:,.2f} {currency1} = {usd_value1:,.2f} USD")
                    print(f"{amount:,.2f} {currency2} = {usd_value2:,.2f} USD")

                    if usd_value1 > usd_value2:
                        print(f"\n{currency1} is stronger than {currency2}.")
                    elif usd_value1 < usd_value2:
                        print(f"\n{currency2} is stronger than {currency1}.")
                    else:
                        print("\nBoth currencies have equal strength.")
                
                except ValueError:
                    print('Error: Invalid input. Please enter a valid number.')
                except Exception as e:
                    print(f"Error: {e}")

            elif choice == "4":
                clear_screen()
                print(f"\n────────────🌍 Current Exchange Rates 🌍────────────")
                print("\nStay informed with the latest currency exchange values:\n")
                for rate in exchange_rates:
                    print(f"{rate}: {exchange_rates[rate]:,.2f}")

            elif choice == "5":
                clear_screen()
                print(f"\n────────────────── ℹ️  About This ℹ️  ────────────────")
                print("\n💡 A simple tool for currency conversion and comparison.\n")
                print("💻 Made by the following programmers:")
                print("1. Fatima A. Pura - CS 1201")
                print("2. Nikki Limboc - CS 1201")
                print("3. Gian Louie Baes - CS 1201")
                print("4. Lance Kert Mendoza - CS 1201")

            elif choice == "6":
                print("\nQuitting...")
                break
            
            else:
                raise ValueError('Invalid option. Please choose a number between 1 and 6.')
            
        except ValueError as e:
            print(f'\nError: {e}')
        
        print('\n───────────────────────────────────────────────────')
        response = input('Back to menu (m) or quit (q)? ').strip().lower()
        if response != 'm':
            print('\nQuitting...')
            break
        else:
            clear_screen()

if __name__ == "__main__":
    main()
