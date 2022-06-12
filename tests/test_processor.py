import pytest
from app.pay.processor import PaymentProcessor


API_KEY = "correct api key, but its BAD to leave it here"


def test_api_key_incalid() -> None:

    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge("1249190007575069", 12, 2026, 100)


def test_card_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2026, 100)


def test_card_invalid_date() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge("1249190007575069", 12, 2000, 100)
