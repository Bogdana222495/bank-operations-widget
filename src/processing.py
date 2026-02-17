from datetime import datetime


def filter_by_state(transactions: list, state: str = "EXECUTED") -> list:
    """Фильтрует список операций по значению 'state'"""
    return [t for t in transactions if t.get("state") == state]


def sort_by_date(transactions: list, reverse: bool = True) -> list:
    """Сортирует список операций по дате (по убыванию по умолчанию)"""
    def parse_date(date_str):
        if not date_str:
            return datetime.min
        date_str = date_str.replace("Z", "")
        # Сначала пробуем с микросекундами
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            pass
        # Потом без микросекунд
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return datetime.min  # fallback на минимальную дату

    return sorted(transactions, key=lambda x: parse_date(x["date"]), reverse=reverse)