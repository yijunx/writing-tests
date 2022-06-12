from app.pay.order import LineItem


def test_line_item_default() -> None:
    line_item = LineItem("test", 100)
    assert line_item.total == 1 * 100


def test_line_item() -> None:
    line_item = LineItem("test", 100, 50)
    assert line_item.total == 50 * 100
