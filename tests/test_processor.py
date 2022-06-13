import pytest
from app.pay.credit_card import CreditCard
from app.pay.processor import PaymentProcessor


API_KEY = "correct api key, but its BAD to leave it here"


def test_api_key_incalid(card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor("")
        processor.charge(card, 100)


def test_card_valid_date(card: CreditCard) -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge(card, 100)


def test_card_invalid_date(expired_card: CreditCard) -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        processor.charge(expired_card, 100)
