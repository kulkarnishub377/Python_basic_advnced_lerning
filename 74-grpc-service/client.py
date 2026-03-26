import time
import grpc
from config import GRPC_SERVER_ADDRESS

try:
    import product_pb2
    import product_pb2_grpc
except ImportError:
    print("[!] Run 'python codegen.py' first to generate the gRPC stubs.")
    raise


def run_client():
    channel = grpc.insecure_channel(GRPC_SERVER_ADDRESS)
    stub = product_pb2_grpc.ProductServiceStub(channel)

    print(f"[Client] Connected to gRPC server at {GRPC_SERVER_ADDRESS}")

    # Create products
    for name, price in [("Laptop", 999.99), ("Phone", 699.99), ("Tablet", 449.99)]:
        resp = stub.CreateProduct(
            product_pb2.CreateProductRequest(name=name, price=price)
        )
        print(f"[Client] CreateProduct(name='{name}', price={price}) -> id={resp.id}")

    # Get a single product
    product = stub.GetProduct(product_pb2.GetProductRequest(id=1))
    print(f"[Client] GetProduct(id=1) -> Product(id={product.id}, name='{product.name}', price={product.price})")

    # List all products
    product_list = stub.ListProducts(product_pb2.Empty())
    print(f"[Client] ListProducts() -> {len(product_list.products)} products found")

    # Benchmark: 100 round-trips
    start = time.perf_counter()
    for _ in range(100):
        stub.ListProducts(product_pb2.Empty())
    elapsed = time.perf_counter() - start
    avg_ms = round(elapsed / 100 * 1000, 1)
    print(f"[Client] 100 gRPC round-trips completed in {elapsed:.2f}s (avg {avg_ms}ms/call)")


if __name__ == "__main__":
    run_client()
