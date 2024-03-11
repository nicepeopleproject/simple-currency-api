import requests
import xml.etree.ElementTree as ET

def get_currency_rate(currency_name):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    
    if response.status_code == 200:
        root = ET.fromstring(response.content)
        
        for valute in root.findall('Valute'):
            name = valute.find('Name').text
            if currency_name.lower() in name.lower():
                rate = valute.find('Value').text
                rate = float(rate.replace(',', '.'))
                return rate
        
        return None
    else:
        return None