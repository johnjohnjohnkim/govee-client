from socket import *
import json

UDP_IP = "239.255.255.250"
SEND_PORT = 4001
LISTEN_PORT = 4002
CONTROL_PORT = 4003

sendSocket = socket(AF_INET, SOCK_DGRAM)
listenSocket = socket(AF_INET, SOCK_DGRAM)
listenSocket.bind(("", LISTEN_PORT))
listenSocket.settimeout(240)

scan_msg = json.dumps({
    "msg": {
        "cmd": "scan",
        "data": {"account_topic": "reserve"}
    }
}).encode()

sendSocket.sendto(scan_msg, (UDP_IP, SEND_PORT))

devices = []

while True:
    try:
        data, addr = listenSocket.recvfrom(1024)
        response = json.loads(data.decode())
        print(f"Got reply from {addr}: {response}")
        devices.append(response["msg"]["data"])
    except timeout:
        print(f"Done scanning. Found {len(devices)} device(s).")
        break