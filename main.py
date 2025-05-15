from abc import ABC, abstractmethod
import os

exchange_rates = {
    'PHP': 0.018,
    'JPY': 0.0069,
    'USD': 1.0,
    'INR': 0.012
}

class Currency(ABC):
    def __init__(self, currency_code, symbol, sub_unit, rate_to_usd, central_bank):
        self.currency_code = currency_code
        self.symbol = symbol
        self.sub_unit = sub_unit
        self.__amount = 0.0
        self._rate_to_usd = rate_to_usd
        self.central_bank = central_bank
    
    def get_amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount

    @abstractmethod
    def convert_to(self, amount, target_currency_code):
        pass

    def compare_with(self, amount, other_currency):
        self_usd = self.convert_to(amount, "USD")
        other_usd = other_currency.convert_to(amount, "USD")

        if self_usd > other_usd:
            return 1
        elif self_usd < other_usd:
            return -1
        else:
            return 0
            
    def __str__(self):
        return (
            f'\n─────────────💵 Currency Information 💵─────────────\n\n'
            f"Currency: {self.currency_code} ({self.symbol})\n"
            f"Subunit: {self.sub_unit}\n"
            f"Exchange Rate to USD: {self._rate_to_usd}\n"
            f"Central Bank: {self.central_bank if self.central_bank else 'N/A'}"
        )

class PhilippinePeso(Currency):
    def __init__(self):
        super().__init__(
        currency_code = "PHP",
        symbol = "₱",
        sub_unit = "Centavos",
        rate_to_usd = exchange_rates['PHP'],
        central_bank = "Bangko Sentral ng Pilipinas"
        )

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

class JapaneseYen(Currency):
    def __init__(self):
        super().__init__(
        currency_code = "JPY",
        symbol = "¥",
        sub_unit = "Sen",
        rate_to_usd = exchange_rates['JPY'],
        central_bank = "Bank of Japan"
        )

    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

class USDollar(Currency):
    def __init__(self):
        super().__init__(
        currency_code = "USD",
        symbol = "$",
        sub_unit = "Cent",
        rate_to_usd = exchange_rates['USD'],
        central_bank = "Federal Reserve"
        )
    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]

class IndianRupee(Currency):
    def __init__(self):
        super().__init__(
        currency_code = "INR",
        symbol = "₹",
        sub_unit = "Paise",
        rate_to_usd = exchange_rates['INR'],
        central_bank = "Bank of India"
        )
    def convert_to(self, amount, target_currency_code):
        usd = amount * self._rate_to_usd
        return usd / exchange_rates[target_currency_code]


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
        raise ValueError("Unsupported currency.")
    

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
                        raise Exception("Unsupported currency.")

                    target_currency_code = input('Enter target currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if target_currency_code not in exchange_rates:
                        raise Exception("Unsupported currency.")

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
                        raise Exception("Unsupported currency.")
                    
                    currency = get_currency_instance(base_currency_code)
                    clear_screen()
                    print(currency)
                    print("\n📊 Converting to all other currencies:")
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
                        raise Exception("Unsupported currency.")

                    currency2 = input('Enter second currency code (PHP, JPY, USD, INR): ').strip().upper()
                    if currency2 not in exchange_rates:
                        raise Exception("Unsupported currency.")

                    currency1_obj = get_currency_instance(currency1)
                    currency2_obj = get_currency_instance(currency2)

                    result = currency1_obj.compare_with(amount, currency2_obj)

                    clear_screen()
                    print("\n─────────────💵 Currency Comparison 💵─────────────")
                    print(f"\nComparing {currency1} and {currency2} (converted to USD):")
                    print(f"💷  {amount:,.2f} {currency1} = {currency1_obj.convert_to(amount, 'USD'):,.2f} USD")
                    print(f"💷  {amount:,.2f} {currency2} = {currency2_obj.convert_to(amount, 'USD'):,.2f} USD")
                    print('\n📊 Result: ', end="")
                    if result == 1:
                        print(f"{currency1} is stronger than {currency2}.")
                    elif result == -1:
                        print(f"{currency2} is stronger than {currency1}.")
                    else:
                        print("Both currencies have equal strength.")

                except ValueError:
                    print('Error: Invalid input. Please enter a valid number.')
                except Exception as e:
                    print(f"Error: {e}")


            elif choice == "4":
                clear_screen()
                print("\n────────────🌍 Current Exchange Rates 🌍────────────")
                print("\nStay informed with the latest currency exchange values:\n")
                for rate in exchange_rates:
                    print(f"✔️  {rate}: {exchange_rates[rate]}")

            elif choice == "5":
                clear_screen()
                print("\n────────────────── ℹ️  About This ℹ️  ────────────────")
                print("\n💡 A simple tool for currency conversion and comparison.\n")
                print("💻 Made by the following programmers:")
                print("1. Fatima A. Pura - CS 1204")
                print("2. Nikki Limboc - CS 1204")
                print("3. Gian Louie Baes - CS 1204")
                print("4. Lance Kert Mendoza - CS 1204")

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
