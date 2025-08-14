"""
Модуль для обработки данных банковских операций.
Содержит функции фильтрации и сортировки по дате и статусу.
"""

from typing import List, Dict, Optional
from datetime import datetime


def filter_by_state(
    operations: List[Dict], state: str = "EXECUTED"
) -> List[Dict]:
    """
    Фильтрует список операций по значению ключа 'state'.

    Args:
        operations: Список словарей с данными о банковских операциях.
        state: Значение ключа 'state' для фильтрации. По умолчанию 'EXECUTED'.

    Returns:
        Список операций, у которых 'state' равен указанному значению.
    """
    return [op for op in operations if op.get("state") == state]


def sort_by_date(
    operations: List[Dict], reverse: bool = True
) -> List[Dict]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с данными о банковских операциях.
        reverse: Порядок сортировки. True — по убыванию (сначала новые), False — по возрастанию.

    Returns:
        Новый отсортированный список операций по дате.
    """
    return sorted(
        operations,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )