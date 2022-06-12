from app.pay.order import Order, LineItem
from app.pay.payment import pay_order
from pytest import MonkeyPatch

from app.pay.processor import PaymentProcessor


def test_pay_order(monkeypatch: MonkeyPatch) -> None:

    def mock_charge(self, card: str, month: int, year: int, amount: int):
        pass

    # replace modules..
    # override the input readings in pay order
    inputs = ["1249190007575069", "12", "2090"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", mock_charge)

    order = Order()
    order.line_items.append(LineItem("Test", 100))

    # to test pay order we need to mock the inputs
    pay_order(order)

    # we dont want the payorder to talk to some server...
    # it should not charge a credit card...

    # it is hard to test, as payment processor is created inside the payorder func
    # so lets mock them

    # ITS BAD...

