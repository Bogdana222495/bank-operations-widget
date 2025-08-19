
import pytest
from src.generators.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]


class TestFilterByCurrency:
    def test_filter_usd(self, transactions):
        usd_gen = filter_by_currency(transactions, "USD")
        result = list(usd_gen)
        assert len(result) == 3
        for trans in result:
            assert trans["operationAmount"]["currency"]["code"] == "USD"

    def test_filter_rub(self, transactions):
        rub_gen = filter_by_currency(transactions, "RUB")
        result = list(rub_gen)
        assert len(result) == 2

    def test_filter_no_match(self, transactions):
        empty_gen = filter_by_currency(transactions, "EUR")
        with pytest.raises(StopIteration):
            next(empty_gen)

    def test_empty_list(self):
        empty_gen = filter_by_currency([], "USD")
        with pytest.raises(StopIteration):
            next(empty_gen)


class TestTransactionDescriptions:
    def test_descriptions(self, transactions):
        desc_gen = transaction_descriptions(transactions)
        expected = [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации"
        ]
        result = [next(desc_gen) for _ in range(5)]
        assert result == expected

    def test_empty_list(self):
        desc_gen = transaction_descriptions([])
        with pytest.raises(StopIteration):
            next(desc_gen)


class TestCardNumberGenerator:
    @pytest.mark.parametrize("start, stop, expected", [
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003"
        ]),
        (9999999999999997, 9999999999999999, [
            "9999 9999 9999 9997",
            "9999 9999 9999 9998",
            "9999 9999 9999 9999"
        ])
    ])
    def test_card_number_generator(self, start, stop, expected):
        gen = card_number_generator(start, stop)
        result = list(gen)
        assert result == expected