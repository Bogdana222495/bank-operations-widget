def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты: 1234 56** **** 7890"""
    if not card_number or not card_number.isdigit():
        return ""
    if len(card_number) == 15:
        # American Express — 15 цифр
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    elif len(card_number) == 16:
        # Обычная карта — 16 цифр
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return ""  # не 15 и не 16 — не маскируем


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта: **XXXX (последние 4 цифры)"""
    if not account_number or not isinstance(account_number, str):
        return ""
    return f"**{account_number[-4:]}"