import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    @pytest.mark.parametrize("input_str, expected", [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счёт 12345678901234567890", "Счёт **7890"),
        ("Visa Platinum 8990922113665859", "Visa Platinum 8990 92** **** 5859"),
        ("Счёт 123", "Счёт **123"),
    ])
    def test_mask_account_card_valid(self, input_str, expected):
        assert mask_account_card(input_str) == expected

    @pytest.mark.parametrize("invalid", [
        "",
        "1234567890123456",
        "Card 1234",
        "Счет 12345678",  # опечатка: "Счет", а не "Счёт"
    ])
    def test_mask_account_card_invalid(self, invalid):
        assert mask_account_card(invalid) == ""


class TestGetDate:
    @pytest.mark.parametrize("iso_string, expected", [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2020-01-01T00:00:00", "01.01.2020"),
        ("2024-12-31T23:59:59", "31.12.2024"),
    ])
    def test_valid_iso_dates(self, iso_string, expected):
        assert get_date(iso_string) == expected

    @pytest.mark.parametrize("invalid", [
        "",
        "abc",
        "2024",
        "11-07-2018",
        None,
    ])
    def test_get_date_invalid(self, invalid):
        assert get_date(invalid) == ""