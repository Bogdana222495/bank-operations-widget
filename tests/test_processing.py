import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def transactions():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2020-01-01T00:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2020-01-02T00:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2020-01-03T00:00:00"},
        {"id": 4, "state": "PENDING", "date": "2020-01-04T00:00:00"},
        {"id": 5, "state": "EXECUTED", "date": "2020-01-02T12:00:00"},
    ]


class TestFilterByState:
    def test_filter_executed(self, transactions):
        result = filter_by_state(transactions, "EXECUTED")
        assert len(result) == 3
        for op in result:
            assert op["state"] == "EXECUTED"

    def test_filter_canceled(self, transactions):
        result = filter_by_state(transactions, "CANCELED")
        assert len(result) == 1
        assert result[0]["state"] == "CANCELED"

    def test_filter_no_match(self, transactions):
        result = filter_by_state(transactions, "FAILED")
        assert len(result) == 0


class TestSortByDate:
    def test_sort_descending(self, transactions):
        result = sort_by_date(transactions, reverse=True)
        dates = [op["date"] for op in result]
        sorted_dates = sorted(dates, reverse=True)
        assert dates == sorted_dates

    def test_sort_ascending(self, transactions):
        result = sort_by_date(transactions, reverse=False)
        dates = [op["date"] for op in result]
        sorted_dates = sorted(dates)
        assert dates == sorted_dates

    def test_sort_with_same_dates(self, transactions):
        subset = [t for t in transactions if t["date"].startswith("2020-01-02")]
        result = sort_by_date(subset, reverse=True)
        # Проверяем по времени: 12:00:00 > 00:00:00
        assert result[0]["id"] == 5  # более поздняя дата
        assert result[1]["id"] == 2

    def test_empty_list(self):
        assert sort_by_date([]) == []

    def test_invalid_date_format(self):
        data = [
            {"date": "invalid"},
            {"date": "2020-01-01T00:00:00"}
        ]
        result = sort_by_date(data, reverse=True)
        assert result[0]["date"] == "2020-01-01T00:00:00"