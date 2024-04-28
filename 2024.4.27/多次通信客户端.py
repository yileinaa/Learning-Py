import socket
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8080))
text=''
while text != 'bye':
    text = input('请输入交流内容')
    client_socket.send(text.encode('utf-8'))
    if text=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')
    print('收到响应',info)
client_socket.close()