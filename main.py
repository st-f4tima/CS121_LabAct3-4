from abc import ABC, abstractmethod

class Currency(ABC):
    def __init__(self, currency_name, amount, target_currency):
        self.__currency_name = currency_name
        self.__amount = amount
        self.target_currency = target_currency
    
    @property
    def amount(self):
        return self.__amount
    
    @property
    def currency_name(self):
        return self.__currency_name
    
    @abstractmethod
    def get_symbol(self):
        pass
    
    @abstractmethod
    def convert_to(self, target_currency):
        pass

    def compare_with(self, other_currency, basis_currency):
        converted_self = self.convert_to(basis_currency)
        converted_other = other_currency.convert_to(basis_currency)

        if converted_self > converted_other:
            return f'{self.get_symbol()} is stronger than {other_currency.get_symbol()} in {basis_currency}'
        elif converted_self < converted_other:
            return f'{self.get_symbol()} is weaker than {other_currency.get_symbol()} in {basis_currency}'
        else:
            return f'{self.get_symbol()} and {other_currency.get_symbol()} are equal in value in {basis_currency}'
    def __str__(self):
        return f'Amount entered: {self.get_symbol()}{self.__amount} (Code: {self.__currency_name})\nConverted to {self.target_currency}: {self.convert_to(self.target_currency)}'

converted_rates = {
    'PHP': 0.018,
    'JPY': 0.0067,
    'USD': 1.0,
    'INR': 0.12
}

# Nikki Limboc
class PhilippinePeso(Currency):
    def __init__(self, currency_name, amount, target_currency, sub_unit):
        super().__init__(currency_name, amount, target_currency)
        self.sub_unit = sub_unit

    def get_symbol(self):
        return "₱"
    
    def convert_to(self, other_currency):
        usd = self.amount * converted_rates['PHP']
        return usd / converted_rates[other_currency]
    
# Gian Baes
class JapaneseYen(Currency):
    def __init__(self, currency_name, amount, target_currency):
        super().__init__(currency_name, amount, target_currency)
    
    def get_symbol(self):
        return "¥"
    
    def convert_to(self, other_currency):
        usd = self.__amount * converted_rates['JPY']
        return usd / converted_rates[other_currency]

# Fatima Pura
class USDollar(Currency):
    def __init__(self, currency_name, amount, target_currency, sub_unit):
        super().__init__(currency_name, amount, target_currency)
        self.sub_unit = sub_unit
    
    def get_symbol(self):
        return "$"
    
    def convert_to(self, other_currency):
        usd = self.__amount * converted_rates['USD']
        return usd / converted_rates[other_currency]

# Lance Mendoza
class IndianRupee(Currency):
    def __init__(self, currency_name, amount, target_currency, sub_unit):
        super().__init__(currency_name, amount, target_currency)
        self.sub_unit = sub_unit

    def get_symbol(self):
        return "₹"
    
    def convert_to(self, other_currency):
        usd = self.__amount * converted_rates['INR']
        return usd / converted_rates[other_currency]

def main():
    try:
        amount = float(input('Enter amount: '))
        currency_name = input('Enter currency code (PHP, JPY, USD, INR): ').strip().upper()
        target_currency = input('Enter target currency code (PHP, JPY, USD, INR): ').strip().upper()

        if currency_name not in converted_rates:
            print('Unsupported currency.')
            return
        
        if currency_name == 'PHP':
            currency = PhilippinePeso(currency_name, amount, target_currency, "Sentimo")
        elif currency_name == 'JPY':
            currency = JapaneseYen(currency_name, amount, target_currency)
        elif currency_name == 'USD':
            currency = USDollar(currency_name, amount, target_currency, "Cent")
        elif currency_name == 'INR':
            currency = IndianRupee(currency_name, amount, target_currency, "Paise")
        else:
            print("Unsupported currency.")
            return

        print(currency)

    except ValueError as e:
        print(f'Error: {e}')

        


if __name__ == "__main__":
    main()