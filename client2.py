import socket
import threading

HOST = 'localhost'
PORT = 8569

nickname = input("Enter your nickname: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.send(nickname.encode('ascii'))
target = input("Enter the recipient: ")
client_socket.send(target.encode('ascii'))


def receive():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("An error occurred!")
            client_socket.close()
            break


def write():
    while True:
        message = input(f"write your msg to << {target} >> :")
        packet = f"\n----- recive msg from  << {nickname} >> : {message}\n"
        client_socket.send(packet.encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()