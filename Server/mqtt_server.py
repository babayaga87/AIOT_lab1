import paho.mqtt.client as mqtt
import json
from db_utils import save_to_db

BROKER = "127.0.0.1"  
PORT = 1883           
TOPIC = "iot/sensor/temperature_humidity" 

def on_connect(client, userdata, flags, rc):
    print(f"Đã kết nối tới MQTT Broker (Mã trạng thái: {rc})")
    client.subscribe(TOPIC)
    print(f"Đang lắng nghe dữ liệu trên topic: {TOPIC}")

def on_message(client, userdata, msg):
    try:
        data_str = msg.payload.decode("utf-8")
        data = json.loads(data_str)
        
        save_to_db(data["device_id"], data["temperature"], data["humidity"], "MQTT", data["timestamp"])
        print(f"Đã nhận và lưu DB: {data}")
    except Exception as e:
        print(f"Lỗi khi xử lý dữ liệu: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.loop_forever()