import socket
import threading

def thread_function(conn, addr):
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if data.decode() == 'close': break
        conn.send(data)
        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('0.0.0.0', 2222))
    s.listen(10)
    for i in range(10):
        conn, addr = s.accept()
        threading.Thread(target=thread_function, args=(conn, addr)).start()
