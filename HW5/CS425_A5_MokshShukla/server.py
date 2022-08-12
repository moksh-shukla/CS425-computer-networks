from ntpath import join
from socket import *
from threading import Thread
import sys

addr = {}
clients = {}

exitMsg = "exit\n"

serHost = str(sys.argv[1])
serPort = int(sys.argv[2])
buffSize = 2048

def clientHandle(client):
    name = client.recv(buffSize).decode()[:-1]
    welcomeMsg = "Welcome "+ str(name) +"! Type exit to leave the chatroom."
    client.send(welcomeMsg.encode())
    joinMsg = str(name) + " has joined the chat."
    broadcastMsg(joinMsg)
    clients[client] = name

    while True:
        msg = client.recv(buffSize).decode()
        if msg:
            if msg != exitMsg:
                broadcastMsg(msg, name + ": ")
            else:
                client.send(exitMsg.encode())
                client.close()
                print(f'Connection from {addr[client]} is closed')
                del clients[client]
                broadcastMsg(f'{name} has left the chat.')
                break
        else:
            client.close()
            print(f'Connection from {addr[client]} is closed')
            del clients[client]
            broadcastMsg(f'{name} has left the chat.')
            break
        
def broadcastMsg(msg, prefix=''):
    for client in clients:
        client.send((prefix + msg).encode())

serSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
serSocket.bind((serHost, serPort))
serSocket.listen()
print('The server is ready to receive. Waiting for connection...')
while True:
    clientocket, clientAddr = serSocket.accept()
    print(f'Connection from {clientAddr} is established')
    clientocket.send('Welcome to the chat room! Enter your name.'.encode())
    addr[clientocket] = clientAddr
    Thread(target=clientHandle, args=(clientocket,)).start()
serSocket.close()