import socket
import threading
from datetime import datetime

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = "127.0.0.1"  # Server's IP address
port = 12345
client_socket.connect((host, port))

# Get the user's username
username = input("Enter your username: ")
client_socket.send(username.encode('utf-8'))

# Function to send messages
def send_message():
    while True:
        message = input()
        timestamp = datetime.now().strftime('[%m/%d/%y %H:%M]')  # Get current time in MM/DD/YY HH:MM format
        message_with_timestamp = f"{username}: {message} {timestamp}"
        client_socket.send(message_with_timestamp.encode('utf-8'))

# Function to receive messages
def receive_message():
    while True:
        try:
            message = client_socket.recv(1024)
            print(message.decode('utf-8'))
        except:
            print("Connection lost")
            break

# Create threads for sending and receiving messages
send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

# Start the threads
send_thread.start()
receive_thread.start()