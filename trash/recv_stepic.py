import socket
req = bytearray(b'close')
s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 2222))
s.send(req)
rsp = s.recv(1024)
print(rsp)
s.close()