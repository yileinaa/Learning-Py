from socket import socket, AF_INET, SOCK_DGRAM
server=socket(AF_INET,SOCK_DGRAM)
server.bind(('127.0.0.1',5040))
text,addr=server.recvfrom(1024)
print('接收到:',text.decode('utf-8'))
data=input('请输入回复')
server.sendto(data.encode('utf-8'),addr)
server.close()
