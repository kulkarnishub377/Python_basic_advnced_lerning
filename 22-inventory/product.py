class Product:
    """
    Models a structural retail product explicitly demonstrating 
    @classmethods, @staticmethods, and Dunder comparisons.
    """
    
    # Class-Level Constant shared uniformly across all physical instances natively
    LOW_STOCK_THRESHOLD = 5

    def __init__(self, sku, name, price, stock):
        self.sku = sku
        self.name = name
        self.price = price
        self.stock = stock

    @classmethod
    def from_dict(cls, data_dict):
        """
        A Class Method acts natively as an Alternative Constructor!
        Instead of calling Product("001", "Milk", 2.0, 10), 
        we directly map JSON dictionaries securely: Product.from_dict({...})
        """
        return cls(
            sku=data_dict["sku"],
            name=data_dict["name"],
            price=data_dict["price"],
            stock=data_dict["stock"]
        )

    def to_dict(self):
        """Standard method explicitly serializing Object Variables onto text."""
        return {
            "sku": self.sku,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    @property
    def is_low_stock(self):
        # We explicitly evaluate mathematically our Class-Level constant dynamically!
        return self.stock <= self.LOW_STOCK_THRESHOLD

    def __lt__(self, other):
        """
        Dunder magic! Determines explicitly how `product_a < product_b` evaluates.
        We sort purely upon numerical inventory stock logic natively.
        """
        return self.stock < other.stock
