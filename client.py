import socket
import time

class DIDS_Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def send_log(self, log):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            client_socket.sendall(log.encode('utf-8'))

if __name__ == "__main__":
    client = DIDS_Client('127.0.0.1', 9999)

    # Simulate sending logs every 2 seconds
    while True:
        log_data = "Network log data here"
        client.send_log(log_data)
        time.sleep(2)

