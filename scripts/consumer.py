from confluent_kafka import Consumer
import sys

# Kafka configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to topic
consumer.subscribe(['user_activity'])

# Poll for messages
while True:
    print("Polling for messages...")  # Log para verificar se está tentando receber
    msg = consumer.poll(1.0)  # Timeout de 1 segundo
    if msg is None:
        print("No message received...")  # Caso não receba nada
        continue
    if msg.error():
        print(f"Error: {msg.error()}")
        continue
    print(f"Received message: {msg.value().decode('utf-8')}")
