from socket import *
import json

UDP_IP = "239.255.255.250"
PORT = 4001

clientSocket = socket(AF_INET, SOCK_DGRAM)

scan_msg = json.dumps({
    "msg": {
        "cmd": "scan",
        "data": {"account_topic": "reserve"}
    }
}).encode()

clientSocket.sendto(scan_msg, (UDP_IP, PORT))

while True:
    data, addr = clientSocket.recvfrom(1024)
    print(f"Got reply from {addr}: {data.decode()}")
