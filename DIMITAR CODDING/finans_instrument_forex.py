from forex_python.converter import CurrencyRates

c = CurrencyRates()

amount = int(input('Enter the amount of currency:  '))

from_currency = input('From currency: ').upper()
to_currency = input('To currency: ').upper()  # Викаме .upper() дали с малки дали с големи ще въведе всички



result = c.convert(from_currency, to_currency, amount)
# print(f'RESULT --> {result}')
profit = f'{float(result) - (float(result) * 0.02):.2f}' # взимаме с 2 процента - даваме е с +

print(amount,from_currency, '--->', result, to_currency )