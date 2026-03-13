import paho.mqtt.client as mqtt
import json
import random
import time
from datetime import datetime

BROKER = "127.0.0.1"
PORT = 1883
TOPIC = "iot/sensor/temperature_humidity"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

print("Bắt đầu mô phỏng Node IoT gửi dữ liệu qua MQTT...")

for i in range(5):
    data = {
        "device_id": "sensor_mqtt_01",
        "temperature": round(random.uniform(25.0, 35.0), 2),
        "humidity": round(random.uniform(50.0, 80.0), 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    payload = json.dumps(data)
    client.publish(TOPIC, payload)
    
    print(f"[{i+1}/5] Đã Publish lên {TOPIC}: {payload}")
    time.sleep(2)

client.disconnect()
print("Hoàn tất phiên gửi dữ liệu.")