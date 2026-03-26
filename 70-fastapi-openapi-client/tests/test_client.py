import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from client import ApiClient
except ImportError:
    print("[!] client.py not found. Please run `python generate_client.py` first!")
    sys.exit(1)

def main():
    print("--- Testing Auto-Generated API Client ---")
    
    # 1. Initialize the SDK
    api = ApiClient()
    
    # 2. Create a product (uses the auto-generated method name based on openapi operationId)
    # The default operation id for FastAPI is <function_name>_post
    print("\n[*] Creating a new product...")
    new_product = api.create_product_products_post(payload={
        "name": "Mechanical Keyboard",
        "price": 129.99,
        "description": "Clicky switches"
    })
    print(f"Created: {new_product}")
    
    # 3. Fetch all products
    print("\n[*] Fetching all products...")
    all_products = api.get_products_products_get()
    print(f"Products: {all_products}")
    
    # 4. Fetch specific product by ID
    product_id = new_product['id']
    print(f"\n[*] Fetching product ID {product_id}...")
    single_product = api.get_product_by_id_products__product_id__get(product_id=product_id)
    print(f"Found: {single_product}")
    
    api.close()
    print("\n--- Test Complete ---")

if __name__ == "__main__":
    main()
