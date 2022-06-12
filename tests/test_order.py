from app.pay.order import Order, LineItem, OrderStatus


def empty_order_total() -> None:
    order = Order()
    assert order.total == 0


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem("x", 50, 100))
    assert order.total == 50 * 100


def test_order_pay() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID
