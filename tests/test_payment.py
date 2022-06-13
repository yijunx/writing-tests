from app.pay.credit_card import CreditCard
from app.pay.order import Order, LineItem
from app.pay.payment import pay_order

# from app.pay.processor import PaymentProcessor
# do not import here but use protocal
# so not reply on it.

class PaymentProcessorMock:
    def charge(self, card: str, amount: int):
        print(f"charging {card} with amount {amount}")


def test_pay_order(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 100))

    # use dependency injection
    pay_order(order, card, PaymentProcessorMock())
