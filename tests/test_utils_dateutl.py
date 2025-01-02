import pytest
from data_market_index_fetcher.indexes.ibov.utils.DateUtil import DateUtil
from datetime import datetime

class TestDateUtil:

    def test_parse_valid_date(self):
        # Test if a valid date string is parsed correctly
        date_string = "2024-12-30"
        expected_result = True
        result = DateUtil.is_valid_date(date_string)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    def test_parse_invalid_date(self):
        # Test if an invalid date string raises an exception
        invalid_date_string = "invalid-date"
        expected_result = False
        result = DateUtil.is_valid_date(invalid_date_string)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"
    
    def test_notinformed_date(self):
        # Test if an invalid date string raises an exception
        invalid_date_string = None
        expected_result = False
        result = DateUtil.is_valid_date(invalid_date_string)
        assert result == expected_result, f"Expected {expected_result}, but got {result}"
    