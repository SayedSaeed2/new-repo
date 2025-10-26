import time
import random
import paho.mqtt.publish as publish

# MQTT Broker address (change if needed)
MQTT_BROKER = "localhost"

# Publish temperature every 5 seconds
while True:
    # Generate random temperature between 60 and 90 degrees
    temp = 60 + random.random() * 30
    print(f"Publishing temperature: {temp:.2f} °C")

    # Publish to MQTT topic
    publish.single("plant1/motor/temp", f"{temp:.2f}", hostname=MQTT_BROKER)

    time.sleep(5)