from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("cannot pay an order with total zero")
    card = input("pls enter your card number: ")
    month = int(input("pls enter a card exp month: "))
    year = int(input("pls enter the card exp year: "))
    payment_processor = PaymentProcessor("6cbbubo-nui7f-asdf4-98h87nyc3")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()
