from socket import socket, AF_INET, SOCK_STREAM
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(5)
client1,client_addr = server_socket.accept()
print('-------连接成功--------')
info = client1.recv(1024).decode('utf-8')
while info != 'bye':
    if info == '':
        print('接收到:',info)
    data=input('请输入回复')
    client1.send(data.encode('utf-8'))
    if info == 'bye':
        break
    info=client1.recv(1024).decode('utf-8')
client1.close()
