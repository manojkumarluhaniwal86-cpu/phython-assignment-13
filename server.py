import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Server is waiting for connection...")

client_socket, address = server.accept()
print(f"Connected with {address}")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(f"\nClient: {message}")
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input("You: ")
    client_socket.send(message.encode())

    if message.lower() == "exit":
        break

client_socket.close()
server.close()
