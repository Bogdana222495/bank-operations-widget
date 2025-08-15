"""
Модуль processing содержит функции для фильтрации и сортировки банковских операций.
"""

from typing import List, Dict, Optional
from datetime import datetime


def filter_by_state(
    operations: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Args:
        operations (List[Dict]): Список словарей с данными о банковских операциях.
        state (str): Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        List[Dict]: Новый список, содержащий только операции с указанным значением 'state'.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict], reverse: bool = True
) -> List[Dict]:
    """
    Сортирует список операций по дате в указанном порядке.

    Args:
        operations (List[Dict]): Список словарей с данными о банковских операциях.
        reverse (bool): Порядок сортировки. True — по убыванию (сначала новые), False — по возрастанию.
                        По умолчанию True.

    Returns:
        List[Dict]: Новый отсортированный список операций по дате.
    """
    return sorted(
        operations,
        key=lambda op: datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )
from src.processing import filter_by_state

# Пример данных
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

# Проверка: фильтруем по 'EXECUTED' (по умолчанию)
result = filter_by_state(data)
print(result)
# Должно вывести только две операции со статусом 'EXECUTED'

# Проверка: фильтруем по 'CANCELED'
result2 = filter_by_state(data, "CANCELED")
print(result2)
# Должно вывести только одну операцию со статусом 'CANCELED'
from datetime import datetime
from typing import List, Dict


def sort_by_date(
    operations: List[Dict], reverse: bool = True
) -> List[Dict]:
    """
    Сортирует список операций по дате в указанном порядке.

    Args:
        operations (List[Dict]): Список словарей с данными о банковских операциях.
        reverse (bool): Порядок сортировки.
                        True — по убыванию (сначала новые),
                        False — по возрастанию (сначала старые).
                        По умолчанию True.

    Returns:
        List[Dict]: Новый отсортированный список операций по дате.
    """
    return sorted(
        operations,
        key=lambda op: datetime.strptime(op["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )