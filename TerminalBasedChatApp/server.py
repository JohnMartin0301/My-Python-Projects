import socket
import threading

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = "127.0.0.1"  # Loopback address
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

clients = []


def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send data
                remove(client)


def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)


def handle_client(client_socket):
    # Ask the client for their username
    client_socket.send("You are now connected. ".encode('utf-8'))
    username = client_socket.recv(1024).decode('utf-8')
    welcome_message = f"{username} has joined the chat."
    broadcast(welcome_message.encode('utf-8'), client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                broadcast(f"{username} has left the chat.".encode('utf-8'), client_socket)
        except:
            continue


while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f"Connection established with {client_address}")
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()