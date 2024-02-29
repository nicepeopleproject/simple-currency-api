from flask import Flask, request, jsonify, render_template
import requests
from xml.etree import ElementTree as ET
from datetime import datetime


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/get_currency_rate', methods=['POST'])
def get_currency_rate():
    currency_name = request.json.get('currency_name')

    if currency_name is None:
        return jsonify({'error': 'Currency name is missing in request'}), 400

    current_date = datetime.now().strftime('%d/%m/%Y')
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            root = ET.fromstring(response.content)
            for valute in root.findall('Valute'):
                if valute.find('CharCode').text == currency_name.upper():
                    rate = float(valute.find('Value').text.replace(',', '.')) / float(valute.find('Nominal').text)
                    return jsonify({'currency_name': currency_name.upper(), 'rate_to_rub': rate})
            return jsonify({'error': 'Currency not found'}), 404
        else:
            return jsonify({'error': 'Failed to fetch data from the server'}), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
