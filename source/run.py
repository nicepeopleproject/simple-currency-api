from main import get_currency_rate
# Пример использования функции для получения курса выбранной валюты к рублю
currency_name = input("Введите название валюты (в установленом банком РФ названием: например, Доллар США): ")
rate_to_rub = get_currency_rate(currency_name)

if rate_to_rub:
    print(f'Текущий курс {currency_name} к рублю: {rate_to_rub}')
else:
    print('Курс для введенной валюты не найден')