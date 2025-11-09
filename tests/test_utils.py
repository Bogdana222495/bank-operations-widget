import json
from unittest.mock import patch, mock_open
from src.utils import get_transactions_from_json


def test_get_transactions_from_json_success():
    mock_data = [{"id": 1, "amount": 100}]
    with patch("src.utils.Path") as MockPath:
        mock_path = MockPath.return_value
        mock_path.exists.return_value = True
        mock_path.open = mock_open(read_data=json.dumps(mock_data))
        result = get_transactions_from_json("fake.json")
        assert result == mock_data


def test_get_transactions_from_json_file_not_found():
    with patch("src.utils.Path") as MockPath:
        mock_path = MockPath.return_value
        mock_path.exists.return_value = False
        result = get_transactions_from_json("missing.json")
        assert result == []


def test_get_transactions_from_json_invalid_json():
    with patch("src.utils.Path") as MockPath:
        mock_path = MockPath.return_value
        mock_path.exists.return_value = True
        mock_path.open = mock_open(read_data="invalid")
        result = get_transactions_from_json("bad.json")
        assert result == []