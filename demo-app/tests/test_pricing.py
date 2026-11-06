"""Baseline tests. These pass with the bugs in place: they never cover a
multi-item coupon order or an order of exactly $75. The engineer agent adds
the tests that catch each customer's case."""

from shop import LineItem, checkout_total


def test_single_item_no_coupon():
    r = checkout_total([LineItem("Mug", 12.00)])
    assert r["subtotal"] == 12.00
    assert r["discount"] == 0.0
    assert r["shipping"] == 6.99
    assert r["tax"] == 0.96
    assert r["total"] == 19.95


def test_single_item_with_coupon():
    r = checkout_total([LineItem("Lamp", 50.00)], coupon="SAVE10")
    assert r["discount"] == 5.00
    assert r["shipping"] == 6.99


def test_big_order_ships_free():
    r = checkout_total([LineItem("Chair", 120.00)])
    assert r["shipping"] == 0.0


def test_unknown_coupon_ignored():
    r = checkout_total([LineItem("Mug", 12.00)], coupon="FREEBIE")
    assert r["discount"] == 0.0
