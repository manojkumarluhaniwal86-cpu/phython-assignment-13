import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to Server")

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message:
                break
            print(f"\nServer: {message}")
        except:
            break

threading.Thread(target=receive_messages, daemon=True).start()

while True:
    message = input("You: ")
    client.send(message.encode())

    if message.lower() == "exit":
        break

client.close()
