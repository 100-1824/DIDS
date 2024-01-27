import socket
import threading

class DIDS_Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.lock = threading.Lock()

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()

    def handle_client(self, client_socket):
        with self.lock:
            self.clients.append(client_socket)

        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                with self.lock:
                    self.clients.remove(client_socket)
                print(f"Connection from {client_socket.getpeername()} closed.")
                break

            print(f"Received log from {client_socket.getpeername()}: {data}")
            # Add your intrusion detection logic here

if __name__ == "__main__":
    server = DIDS_Server('127.0.0.1', 9999)
    server.start_server()

