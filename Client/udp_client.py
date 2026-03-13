import socket
import json
import random
from datetime import datetime, time

HOST = "127.0.0.1"   # doi thanh IP server neu can
PORT = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
device_id = f"device_{random.randint(1, 100)}"
while True:
    temperature = round(random.uniform(20.0, 30.0), 2)
    humidity = round(random.uniform(30.0, 70.0), 2)
    timestamp = datetime.now().isoformat()

    msg = {
        "device_id": device_id,
        "temperature": temperature,
        "humidity": humidity,
        "timestamp": timestamp
    }
    s.sendto(json.dumps(msg).encode("utf-8"), (HOST, PORT))
    print(f"Da gui du lieu UDP: {msg}")
    data, _ = s.recvfrom(1024)
    print("Phan hoi tu server UDP:", data.decode("utf-8"))
    # Gui du lieu moi sau 5 giay
    time.sleep(5)

    
