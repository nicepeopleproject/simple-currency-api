from flask import Flask, request, jsonify
import requests
from xml.etree import ElementTree as ET

app = Flask(__name__)

def get_currency_rate(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    root = ET.fromstring(response.content)
    for valute in root.findall('Valute'):
        if valute.find('CharCode').text == currency:
            return float(valute.find('Value').text.replace(',', '.'))

@app.route('/get_currency_rate', methods=['POST'])
def get_currency_rate_handler():
    currency = request.json.get('currency')
    if currency is None:
        return jsonify({'error': 'На дана валюта'}), 400
    rate = get_currency_rate(currency)
    if rate is None:
        return jsonify({'error': 'Валюта не найдена'}), 404
    return jsonify({'currency': currency, 'rate': rate})

if __name__ == '__main__':
    app.run(debug=True)