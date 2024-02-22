import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QDateEdit, QLabel, QTableWidget, QTableWidgetItem, QTabWidget, QComboBox, QLineEdit
from PyQt5.QtCore import QDate
import requests
from xml.etree import ElementTree

class CurrencyViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Currency Viewer')
        self.setGeometry(100, 100, 800, 600)
        
        self.tabWidget = QTabWidget(self)
        self.setCentralWidget(self.tabWidget)
        
        self.createCurrencyRateTab()
        self.createCurrencyConverterTab()
    
    def createCurrencyRateTab(self):
        self.currencyRateTab = QWidget()
        self.tabWidget.addTab(self.currencyRateTab, "Курс валют")
        
        layout = QVBoxLayout()
        
        self.dateEdit = QDateEdit()
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDate(QDate.currentDate())
        layout.addWidget(self.dateEdit)
        
        self.loadButton = QPushButton('Загрузить курс валют')
        self.loadButton.clicked.connect(self.loadCurrencyRates)
        layout.addWidget(self.loadButton)
        
        self.currencyTable = QTableWidget()
        self.currencyTable.setColumnCount(4)
        self.currencyTable.setHorizontalHeaderLabels(['Шифр', 'Номинал', 'Название', 'Стоимость'])
        layout.addWidget(self.currencyTable)
        
        self.currencyRateTab.setLayout(layout)
    
    def createCurrencyConverterTab(self):
        self.currencyConverterTab = QWidget()
        self.tabWidget.addTab(self.currencyConverterTab, "Обмен валют")
        
        layout = QVBoxLayout()
        
        self.fromCurrencyComboBox = QComboBox()
        self.toCurrencyComboBox = QComboBox()
        
        self.amountLineEdit = QLineEdit()
        self.amountLineEdit.setPlaceholderText("Сколько конвертнуть?")
        
        self.convertButton = QPushButton("Конвертировать")
        self.convertButton.clicked.connect(self.convertCurrency)
        
        self.resultLabel = QLabel("Итог: ")
        
        layout.addWidget(QLabel("Из:"))
        layout.addWidget(self.fromCurrencyComboBox)
        layout.addWidget(QLabel("В:"))
        layout.addWidget(self.toCurrencyComboBox)
        layout.addWidget(self.amountLineEdit)
        layout.addWidget(self.convertButton)
        layout.addWidget(self.resultLabel)
        
        self.currencyConverterTab.setLayout(layout)

    def loadCurrencyRates(self):
        date = self.dateEdit.date().toString('dd/MM/yyyy')
        url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}'
        response = requests.get(url)
        
        self.fromCurrencyComboBox.clear()
        self.toCurrencyComboBox.clear()
        self.fromCurrencyComboBox.addItem("RUB", 1)
        self.toCurrencyComboBox.addItem("RUB", 1)
        
        if response.status_code == 200:
            xml_data = response.text
            root = ElementTree.fromstring(xml_data)
            self.currencyTable.setRowCount(0)
            
            for valute in root.findall('Valute'):
                rowPosition = self.currencyTable.rowCount()
                self.currencyTable.insertRow(rowPosition)
                
                charCode = valute.find('CharCode').text
                nominal = valute.find('Nominal').text
                name = valute.find('Name').text
                value = valute.find('Value').text.replace(',', '.')
                
                self.currencyTable.setItem(rowPosition, 0, QTableWidgetItem(charCode))
                self.currencyTable.setItem(rowPosition, 1, QTableWidgetItem(nominal))
                self.currencyTable.setItem(rowPosition, 2, QTableWidgetItem(name))
                self.currencyTable.setItem(rowPosition, 3, QTableWidgetItem(value))
                
                self.fromCurrencyComboBox.addItem(charCode, float(value)/float(nominal))
                self.toCurrencyComboBox.addItem(charCode, float(value)/float(nominal))
        else:
            print('Ошибка получения курсов валют')

    def convertCurrency(self):
        amount = self.amountLineEdit.text()
        try:
            amount = float(amount)
            fromCurrency = self.fromCurrencyComboBox.currentText()
            toCurrency = self.toCurrencyComboBox.currentText()
            fromRate = self.fromCurrencyComboBox.currentData()
            toRate = self.toCurrencyComboBox.currentData()
            result = amount * (fromRate / toRate)
            self.resultLabel.setText(f"Итог: {amount} {fromCurrency} = {result:.2f} {toCurrency}")
        except ValueError:
            self.resultLabel.setText("Введите значение")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = CurrencyViewer()
    mainWin.show()
    sys.exit(app.exec_())
