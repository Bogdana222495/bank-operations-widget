from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует карту или счёт в зависимости от типа"""
    if not info or not isinstance(info, str):
        return ""
    info = info.strip()
    if not info:
        return ""

    parts = info.rsplit(" ", 1)
    if len(parts) != 2:
        return ""

    prefix, number = parts
    if not number.isdigit():
        return ""

    if prefix.startswith("Счёт"):
        return f"{prefix} {get_mask_account(number)}"
    else:
        masked = get_mask_card_number(number)
        if masked:
            return f"{prefix} {masked}"
        return ""


def get_date(iso_string: str) -> str:
    """Преобразует ISO-формат даты (2020-01-01T12:34:56) в ДД.ММ.ГГГГ"""
    if not iso_string or not isinstance(iso_string, str):
        return ""
    try:
        if "T" not in iso_string:
            return ""
        date_part = iso_string.split("T")[0]
        year, month, day = date_part.split("-")
        if len(year) == 4 and len(month) == 2 and len(day) == 2:
            return f"{day}.{month}.{year}"
        return ""
    except Exception:
        return ""