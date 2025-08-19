
def filter_by_currency(transactions: list, currency: str):
    """
    Генератор, возвращающий транзакции с указанной валютой.

    :param transactions: Список словарей с транзакциями
    :param currency: Код валюты (например, "USD")
    :yields: Словарь с транзакцией
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list):
    """
    Генератор, возвращающий описания транзакций по очереди.

    :param transactions: Список словарей с транзакциями
    :yields: Описание транзакции (строка)
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int):
    """
    Генератор, возвращающий номера карт в формате XXXX XXXX XXXX XXXX.
    Обрезает слишком большие числа до 16 цифр с конца.

    :param start: Начальное число (включительно)
    :param stop: Конечное число (включительно)
    :yields: Строка с номером карты
    """
    for number in range(start, stop + 1):
        card_str = str(number)
        # Оставляем только последние 16 цифр
        if len(card_str) > 16:
            card_str = card_str[-16:]
        # Дополняем нулями слева до 16
        card_str = card_str.zfill(16)
        # Форматируем: XXXX XXXX XXXX XXXX
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:]}"
        yield formatted