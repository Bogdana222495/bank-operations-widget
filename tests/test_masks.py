import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    @pytest.mark.parametrize("card_num, expected", [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("123456781234567", "1234 56** **** 4567"),
    ])
    def test_get_mask_card_number(self, card_num, expected):
        assert get_mask_card_number(card_num) == expected

    def test_get_mask_card_number_empty(self):
        assert get_mask_card_number("") == ""
        assert get_mask_card_number("abc") == ""