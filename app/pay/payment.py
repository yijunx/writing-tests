from typing import Protocol
from app.pay.credit_card import CreditCard
from app.pay.order import Order

# from app.pay.processor import PaymentProcessor
# no dependency on the actual payment processor!!!


class PaymentProcessor(Protocol):
    def charge(self, card: CreditCard, amount: int):
        """charge the card with the amount"""


def pay_order(order: Order, card: CreditCard, payment_processor: PaymentProcessor):
    """here we make processor an argument
    so that pay order does not need to create the processor
    down below. this helps us gain more control of the function,
    this is dependency injection.

    also, the we can apply dependency inversion here. say PaymentProcessor
    is a ABC, and there could be different concrete payment processors.
    """
    if order.total == 0:
        raise ValueError("cannot pay an order with total zero")

    # so no need to create the payment processor here
    # payment_processor = PaymentProcessor("correct api key, but its BAD to leave it here")
    payment_processor.charge(card=card, amount=order.total)
    order.pay()
