import socket
import threading

HOST = 'localhost'
PORT = 8569

account_name = input("Enter your account_name: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(account_name.encode('ascii'))
target = input("Enter the account name you want to talk: ")
client_socket.send(target.encode('ascii'))


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("failed to connect")
            client_socket.close()
            break


def write():
    while True:
        message = input(f"write your msg to << {target} >> :")
        packet = f"\n----- recive msg from  << {account_name} >> : {message}\n"
        client_socket.send(packet.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()