from app.pay.order import Order
from app.pay.processor import PaymentProcessor


def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("cannot pay an order with total zero")
    card = input("pls enter your card number: ")
    month = int(input("pls enter a card exp month: "))
    year = int(input("pls enter the card exp year: "))
    payment_processor = PaymentProcessor("correct api key, but its BAD to leave it here")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()
