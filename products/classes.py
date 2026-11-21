from dataclasses import dataclass, field


@dataclass
class Product:
    """A user-defined class: one product of the catalog."""
    name: str
    price: float
    description: str
    image: str = ''                 # file name inside static/img/
    in_stock: bool = True
    old_price: float | None = None  # set when the product is on sale
    tags: list = field(default_factory=list)

    @property
    def on_sale(self):
        return self.old_price is not None and self.old_price > self.price

    @property
    def discount_percent(self):
        if not self.on_sale:
            return 0
        return round((1 - self.price / self.old_price) * 100)


def summarize(products):
    """Collect statistics about a list of Product objects into a dict."""
    products = list(products)
    prices = [p.price for p in products]
    return {
        'total': len(products),
        'in_stock': sum(1 for p in products if p.in_stock),
        'out_of_stock': sum(1 for p in products if not p.in_stock),
        'on_sale': sum(1 for p in products if p.on_sale),
        'cheapest': min(products, key=lambda p: p.price) if products else None,
        'priciest': max(products, key=lambda p: p.price) if products else None,
        'average': sum(prices) / len(prices) if prices else 0,
    }
