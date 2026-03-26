import json
import os
from product import Product

class Inventory:
    """
    An OOP collection object managing serialization natively writing and reading 
    JSON boundaries explicitly utilizing Python Product parameters.
    """

    def __init__(self):
        self.products = []
        self.data_path = os.path.join(os.path.dirname(__file__), "database.json")
        self._load_database()

    def _load_database(self):
        """Internal structural method."""
        if not os.path.exists(self.data_path):
            self.products = []
            return
            
        with open(self.data_path, "r", encoding="utf-8") as f:
            if os.path.getsize(self.data_path) > 0:
                raw_data = json.load(f)
                # Utilizing our @classmethod alternative constructor beautifully!
                self.products = [Product.from_dict(item) for item in raw_data]

    def save_database(self):
        """Serializes Object arrays structurally back onto Strings natively."""
        raw_data = [p.to_dict() for p in self.products]
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(raw_data, f, indent=4)

    def add_product(self, product):
        if any(p.sku == product.sku for p in self.products):
            return False
        self.products.append(product)
        self.save_database()
        return True

    def process_sale(self, sku, quantity=1):
        for p in self.products:
            if p.sku == sku:
                if p.stock >= quantity:
                    p.stock -= quantity
                    self.save_database()
                    return True, "Sale successful!"
                return False, "Insufficient localized inventory."
        return False, "SKU entirely missing."

    def get_low_stock_alerts(self):
        """List comprehensions evaluating Object properties natively."""
        return [p for p in self.products if p.is_low_stock]
