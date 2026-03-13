import socket
import json
from db_utils import save_to_db

HOST = "0.0.0.0"
PORT = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((HOST, PORT))
    print(f"UDP Server dang lang nghe tai {HOST}:{PORT}")
except OSError as e:
    print(f"Loi: Khong the bind port {PORT}. Co the port da duoc su dung boi tien trinh khac. Loi: {e}")
    exit(1)

while True:
    data, addr = s.recvfrom(1024)
    if data:
        try:
            msg = json.loads(data.decode("utf-8"))
            device_id = msg["device_id"]
            temperature = msg["temperature"]
            humidity = msg["humidity"]
            timestamp = msg["timestamp"]

            save_to_db(device_id, temperature, humidity, "UDP", timestamp)

            print("Da nhan va luu du lieu UDP:", msg)
            s.sendto("Da luu du lieu UDP".encode("utf-8"), addr)
        except Exception as e:
            print("Loi xu ly du lieu UDP:", e)
            s.sendto("Loi xu ly du lieu UDP".encode("utf-8"), addr)
