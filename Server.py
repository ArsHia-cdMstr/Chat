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
            client_socket.send(f"\n{target.decode()} device isn't available .".encode())


def accept_clients():
    while True:
        client_socket, address = server_socket.accept()
        user_account_name = client_socket.recv(1024)
        target_account_name = client_socket.recv(1024)
        clients.append([client_socket, user_account_name, target_account_name])
        # print(clients)
        print(f"A new connection was created with address : << {address} >>  username: << {user_account_name.decode()} >> target: << {target_account_name.decode()} >>")
        client_socket.send("_____________________   Chat Page   _____________________".encode())
        thread = threading.Thread(target=work_with_client, args=(client_socket, address, target_account_name))
        thread.start()


print("Server is on")
accept_thread = threading.Thread(target=accept_clients)
accept_thread.start()
