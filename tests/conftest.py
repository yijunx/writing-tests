import pytest
from app.pay.credit_card import CreditCard
from datetime import date


@pytest.fixture
def card() -> CreditCard:
    return CreditCard("1249190007575069", 12, date.today().year + 2)


@pytest.fixture
def expired_card() -> CreditCard:
    return CreditCard("1249190007575069", 12, 1990)