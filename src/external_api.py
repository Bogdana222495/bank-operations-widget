import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Получаем API-ключ из .env
API_KEY = os.getenv("EXCHANGE_API_KEY")

# Базовый URL для API
BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"


def convert_to_rubles(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Args:
        transaction (dict): Словарь с данными транзакции.

    Returns:
        float: Сумма в рублях.
    """
    # Извлекаем сумму и валюту из транзакции
    amount_str = transaction.get("operationAmount", {}).get("amount", "0")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

    # Преобразуем строку в число
    try:
        amount = float(amount_str)
    except ValueError:
        amount = 0.0

    # Если валюта RUB — возвращаем сумму без изменений
    if currency_code == "RUB":
        return amount

    # Если валюта USD или EUR — конвертируем через API
    elif currency_code in ("USD", "EUR"):
        rate = get_exchange_rate(currency_code)
        return round(amount * rate, 2)

    # Если валюта не поддерживается — возвращаем сумму как есть
    else:
        return amount


def get_exchange_rate(currency: str) -> float:
    """
    Получает курс обмена из API.

    Args:
        currency (str): Код валюты (например, USD).

    Returns:
        float: Курс обмена (сколько RUB за 1 единицу валюты).
    """
    if not API_KEY:
        raise EnvironmentError("API ключ не найден. Проверьте файл .env")

    url = f"{BASE_URL}?base={currency}&symbols=RUB"
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    data = response.json()
    return data["rates"]["RUB"]