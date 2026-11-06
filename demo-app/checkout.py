"""Print a receipt, so a person (or agent) can see a customer's order.

    python checkout.py SAVE10 "Headphones:40" "Cable:15" "Case:25"
"""

import sys

from shop import LineItem, checkout_total


def main(argv: list[str]) -> None:
    coupon = argv[1] if len(argv) > 1 and ":" not in argv[1] else None
    raw = argv[2:] if coupon else argv[1:]
    items = []
    for arg in raw:
        name, price, *qty = arg.split(":")
        items.append(LineItem(name, float(price), int(qty[0]) if qty else 1))
    r = checkout_total(items, coupon)
    for i in items:
        print(f"  {i.name:<14} {i.quantity} x ${i.unit_price:.2f}")
    print(f"  {'Subtotal':<18} ${r['subtotal']:.2f}")
    print(f"  {'Discount':<18} -${r['discount']:.2f}  ({coupon or 'none'})")
    print(f"  {'Shipping':<18} ${r['shipping']:.2f}")
    print(f"  {'Tax':<18} ${r['tax']:.2f}")
    print(f"  {'TOTAL':<18} ${r['total']:.2f}")


if __name__ == "__main__":
    main(sys.argv)
