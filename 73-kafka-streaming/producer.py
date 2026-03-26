import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer
from config import KAFKA_BROKER, TOPIC_NAME

PAGES = ["/home", "/products", "/cart", "/checkout", "/about"]
ELEMENTS = ["buy_button", "add_to_cart", "search_bar", "nav_link", "banner"]
PRODUCTS = [
    ("Laptop", 999.99), ("Phone", 699.99), ("Headphones", 149.99),
    ("Monitor", 449.99), ("Keyboard", 129.99), ("Mouse", 29.99),
]


def create_random_event():
    """Generate a random analytics event."""
    event_type = random.choices(
        ["page_view", "click", "purchase"], weights=[50, 35, 15]
    )[0]

    event = {
        "event_type": event_type,
        "user_id": random.randint(1, 500),
        "timestamp": datetime.utcnow().isoformat(),
    }

    if event_type == "page_view":
        event["page"] = random.choice(PAGES)
    elif event_type == "click":
        event["element"] = random.choice(ELEMENTS)
    elif event_type == "purchase":
        product, price = random.choice(PRODUCTS)
        event["product"] = product
        event["amount"] = price

    return event


def run_producer(num_events: int = 1000):
    """Publish N random analytics events to the Kafka topic."""
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
    except Exception as e:
        print(f"[!] Failed to connect to Kafka at {KAFKA_BROKER}: {e}")
        print("[!] Make sure Kafka is running.")
        return

    print(f"[Producer] Publishing {num_events} events to topic '{TOPIC_NAME}'...")
    start = time.time()

    for i in range(num_events):
        event = create_random_event()
        producer.send(TOPIC_NAME, value=event)

        if (i + 1) % 100 == 0:
            print(f"[Producer] Sent {i + 1}/{num_events} events...")

        time.sleep(0.003)  # Slight delay to simulate real traffic

    producer.flush()
    elapsed = round(time.time() - start, 2)
    print(f"[Producer] {num_events} events published in {elapsed} seconds")


if __name__ == "__main__":
    run_producer()
