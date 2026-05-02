import os
import json
import tempfile
import pytest

from order_system import Order, OrderManager


# -------------------------
# Helpers
# -------------------------


def sample_items():
    """Formato esperado tras el merge."""
    return [
        {"name": "Keyboard", "price": 50, "qty": 1},
        {"name": "Mouse", "price": 25, "qty": 2},
    ]


# -------------------------
# Tests de Order
# -------------------------


def test_total_price_without_discount():
    order = Order(
        order_id=1,
        customer="Alice",
        items=sample_items(),
        discount=0,
    )

    assert order.total_price() == 100


def test_total_price_with_discount():
    order = Order(
        order_id=1,
        customer="Alice",
        items=sample_items(),
        discount=10,
    )

    # subtotal = 100 → 10% descuento → 90
    assert round(order.total_price(), 2) == 90


def test_invalid_discount_raises():
    with pytest.raises(ValueError):
        Order(
            order_id=1,
            customer="Alice",
            items=sample_items(),
            discount=150,
        ).total_price()


def test_summary_contains_expected_fields():
    order = Order(
        order_id=1,
        customer="Alice",
        items=sample_items(),
        discount=5,
    )

    summary = order.summary()

    assert "order_id" in summary or "id" in summary
    assert "customer" in summary
    assert "total" in summary or "total_price" in summary


# -------------------------
# Tests de OrderManager
# -------------------------


def test_create_and_get_order():
    manager = OrderManager()

    manager.create_order(
        1,
        "Alice",
        sample_items(),
        discount=0,
    )

    order = manager.get_order(1)
    assert order is not None
    assert order.customer == "Alice"


def test_total_revenue_multiple_orders():
    manager = OrderManager()

    manager.create_order(1, "Alice", sample_items(), discount=0)
    manager.create_order(2, "Bob", sample_items(), discount=10)

    total = manager.get_total_revenue()

    # 100 + 90 = 190
    assert round(total, 2) == 190


def test_persistence_to_disk():
    with tempfile.TemporaryDirectory() as tmpdir:
        filepath = os.path.join(tmpdir, "orders.json")

        manager = OrderManager(storage_file=filepath)

        manager.create_order(
            1,
            "Alice",
            sample_items(),
            discount=0,
        )

        assert os.path.exists(filepath)

        with open(filepath) as f:
            data = json.load(f)

        assert "1" in data


def test_duplicate_order_id_raises():
    manager = OrderManager()

    manager.create_order(1, "Alice", sample_items(), discount=0)

    with pytest.raises(ValueError):
        manager.create_order(1, "Alice", sample_items(), discount=0)
