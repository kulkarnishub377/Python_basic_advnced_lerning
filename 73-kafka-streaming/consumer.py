import json
from kafka import KafkaConsumer
from config import KAFKA_BROKER, TOPIC_NAME
from aggregator import record_event


def run_consumer():
    """Consume analytics events from Kafka and aggregate metrics."""
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BROKER,
            auto_offset_reset="earliest",
            value_deserializer=lambda v: json.loads(v.decode("utf-8")),
            group_id="analytics_consumer_group",
        )
    except Exception as e:
        print(f"[!] Failed to connect to Kafka at {KAFKA_BROKER}: {e}")
        print("[!] Make sure Kafka is running.")
        return

    print(f"[Consumer] Listening on topic '{TOPIC_NAME}'...")

    for message in consumer:
        event = message.value
        event_type = event.get("event_type", "unknown")
        amount = event.get("amount", 0.0)

        record_event(event_type, amount)
        print(f"[Consumer] Consumed: {event_type} | offset={message.offset}")


if __name__ == "__main__":
    run_consumer()
