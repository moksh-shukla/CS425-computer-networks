import socket,sys,select

max_size = 2048

exitMsg = "exit\n"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print("Correct Usage-> script, <IP address>, <PORT NO>")
    exit() 

serHost = str(sys.argv[1])
serPort = int(sys.argv[2])
addr = (serHost,serPort)
client.connect(addr)

while True:
    read_sockets,write_socket,error_socket = select.select([sys.stdin,client],[],[])
    for socket in read_sockets:
        if socket == client:
            msg = socket.recv(max_size).decode()
            if msg:
                print(msg)
            else:
                print("Connection closed by server")
                sys.exit()
        else:
            msg = sys.stdin.readline()
            client.send(msg.encode())
            if msg == exitMsg:
                client.close()
                sys.exit()