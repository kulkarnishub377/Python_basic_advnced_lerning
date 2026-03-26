from search import create_index, index_product, ES_AVAILABLE

MOCK_PRODUCTS = [
    {"name": "Gaming Laptop Pro", "category": "Electronics", "price": 1499.99, "description": "High-performance gaming laptop with RTX GPU"},
    {"name": "Ultrabook Laptop 14", "category": "Electronics", "price": 899.99, "description": "Lightweight ultrabook for professionals"},
    {"name": "Wireless Mouse", "category": "Accessories", "price": 29.99, "description": "Ergonomic wireless mouse with USB receiver"},
    {"name": "Mechanical Keyboard", "category": "Accessories", "price": 129.99, "description": "RGB mechanical keyboard with Cherry MX switches"},
    {"name": "4K Monitor 27 inch", "category": "Electronics", "price": 449.99, "description": "Ultra HD IPS display monitor"},
    {"name": "USB-C Hub Adapter", "category": "Accessories", "price": 39.99, "description": "7-in-1 USB-C multi-port adapter"},
    {"name": "Noise Cancelling Headphones", "category": "Audio", "price": 299.99, "description": "Over-ear wireless headphones with ANC"},
    {"name": "Portable Bluetooth Speaker", "category": "Audio", "price": 79.99, "description": "Waterproof portable speaker with deep bass"},
    {"name": "Smartwatch Fitness Tracker", "category": "Wearables", "price": 199.99, "description": "GPS smartwatch with heart rate monitoring"},
    {"name": "External SSD 1TB", "category": "Storage", "price": 109.99, "description": "Portable solid state drive with USB 3.2"},
]


def seed():
    if not ES_AVAILABLE:
        print("[!] Elasticsearch is not available. Start it on port 9200 first.")
        return

    print("[*] Creating index...")
    create_index()

    print(f"[*] Indexing {len(MOCK_PRODUCTS)} products...")
    for product in MOCK_PRODUCTS:
        index_product(product)
        print(f"  + Indexed: {product['name']}")

    print("[+] Seeding complete!")


if __name__ == "__main__":
    seed()
