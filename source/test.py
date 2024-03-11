import unittest
from unittest.mock import patch
from main import get_currency_rate
class TestGetCurrencyRate(unittest.TestCase):
    def test_get_currency_rate(self):
        # Проверка работы функции с валютой, которая существует
        rate = get_currency_rate('Доллар США')
        self.assertIsNotNone(rate)

    def test_get_currency_rate1(self):
        # Проверка работы функции с валютой, которая существует
        rate = get_currency_rate('Евро')
        self.assertIsNotNone(rate)

    def test_get_currency_rate2(self):
        # Проверка работы функции с валютой, которая существует
        rate = get_currency_rate('Азербайджанский манат')
        self.assertIsNotNone(rate)

    def test_get_currency_rate_incorrect_currency(self):
        # Проверка работы функции с валютой, которой нет
        rate = get_currency_rate('fake_currency')
        self.assertIsNone(rate)

# запуск тестов
if __name__ == '__main__':
    unittest.main()