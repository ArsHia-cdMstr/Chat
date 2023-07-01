import socket
import threading

HOST = 'localhost'
PORT = 8569

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

clients = []


def work_with_client(client_socket, address, target):
    while True:
        try:
            message = client_socket.recv(1024)
            sender(message, client_socket, target)
        except:
            for client in clients:
                if client[0] == client_socket:
                    clients.remove(client)
                    client_socket.close()
            print(f"Connection closed with {address}")
            break


def sender(message, client_socket, target):
    for client in clients:
        if client[1] == target:
            print(client[0])
            client[0].send(message)
            break
        if client == clients[-1]:
            client_socket.send(f"{target.decode()} is not online.".encode())


def accept_clients():
    while True:
        client_socket, address = server_socket.accept()
        user = client_socket.recv(1024)
        target = client_socket.recv(1024)
        clients.append([client_socket, user, target])
        # print(clients)
        print(f"New connection from {address}-----username: {user.decode()}-----target: {target.decode()}")
        client_socket.send("Welcome to the chat room!".encode())
        thread = threading.Thread(target=work_with_client, args=(client_socket, address, target))
        thread.start()


print("Server started!")
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()
