"""Checkout pricing for the demo shop.

Two bugs are planted here for the Escalation Room demo. Both overcharge
customers, and both are fixed live by the engineer agent. Don't fix them
before recording.
"""

from dataclasses import dataclass

TAX_RATE = 0.08
FREE_SHIPPING_THRESHOLD = 75.00  # policy: free shipping on $75 or more, after discounts
SHIPPING_FEE = 6.99
COUPONS = {"SAVE10": 0.10}  # policy: percent off the whole subtotal


@dataclass
class LineItem:
    name: str
    unit_price: float
    quantity: int = 1


def apply_coupon(items: list[LineItem], coupon: str | None) -> float:
    """Return the discount amount for the order."""
    if not coupon or coupon not in COUPONS or not items:
        return 0.0
    first = items[0]
    return first.unit_price * first.quantity * COUPONS[coupon]


def shipping_for(amount: float) -> float:
    return 0.0 if amount > FREE_SHIPPING_THRESHOLD else SHIPPING_FEE


def checkout_total(items: list[LineItem], coupon: str | None = None) -> dict:
    subtotal = round(sum(i.unit_price * i.quantity for i in items), 2)
    discount = round(apply_coupon(items, coupon), 2)
    after_discount = subtotal - discount
    shipping = shipping_for(after_discount)
    tax = round(after_discount * TAX_RATE, 2)
    total = round(after_discount + tax + shipping, 2)
    return {
        "subtotal": subtotal,
        "discount": discount,
        "shipping": shipping,
        "tax": tax,
        "total": total,
    }
