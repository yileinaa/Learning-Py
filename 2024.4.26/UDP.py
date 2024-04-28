from socket import socket, AF_INET, SOCK_DGRAM
client = socket(AF_INET,SOCK_DGRAM)
text=input("请输入传递内容")
client.sendto(text.encode('utf-8'),('127.0.0.1',5040))
resp,addr=client.recvfrom(1024)
print('接收到；',resp.decode('utf-8'))
client.close()