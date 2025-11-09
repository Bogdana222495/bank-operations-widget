from unittest.mock import patch
from src.external_api import convert_to_rubles


def test_convert_to_rubles_rub():
    """Тест для RUB"""
    transaction = {
        "operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}
    }
    assert convert_to_rubles(transaction) == 1000.0


@patch("src.external_api.get_exchange_rate", return_value=90.0)
def test_convert_to_rubles_usd(mock_rate):
    """Тест для USD"""
    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }
    assert convert_to_rubles(transaction) == 9000.0


@patch("src.external_api.get_exchange_rate", return_value=100.0)
def test_convert_to_rubles_eur(mock_rate):
    """Тест для EUR"""
    transaction = {
        "operationAmount": {"amount": "50", "currency": {"code": "EUR"}}
    }
    assert convert_to_rubles(transaction) == 5000.0