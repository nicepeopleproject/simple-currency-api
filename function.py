import requests
from xml.etree import ElementTree

def get_currency_rate(currency_id, date_req=None):
    # Формирование URL запроса
    base_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    if date_req:
        url = f"{base_url}?date_req={date_req}"
    else:
        url = base_url

    # Отправка запроса
    response = requests.get(url)
    if response.status_code == 200:
        # Парсинг XML
        root = ElementTree.fromstring(response.content)

        # Поиск курса валюты
        for valute in root.findall('Valute'):
            if valute.find('CharCode').text == currency_id:
                nominal = valute.find('Nominal').text
                value = valute.find('Value').text.replace(',', '.')
                return float(value) / float(nominal)


    return None



currency_code = 'EUR'
date_query = '02/03/2023'
rate = get_currency_rate(currency_code, date_query)
if rate:
    print(f"Курс {currency_code} к RUB на {date_query}: {rate}")
else:
    print("Информация о курсе валюты не найдена.")