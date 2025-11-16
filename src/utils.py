import json
from pathlib import Path
from typing import List, Dict, Any


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Считывает список транзакций из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict[str, Any]]: Список транзакций или пустой список при ошибке.
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return []

        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, IOError, ValueError):
        return []