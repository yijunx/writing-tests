from pay.order import LineItem, Order
from pay.payment import pay_order


def main():
    card = input("pls enter your card number: ")
    month = int(input("pls enter a card exp month: "))
    year = int(input("pls enter the card exp year: "))

    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=50_00))
    pay_order(order)


if __name__ == "__main__":
    main()
