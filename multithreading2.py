import threading
import socket
import server1
import server2
from misc import *

class Server(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
    
    def messageHandler(self):
        needRes = False
        if msg == b"name":
            res = getpass.getuser()
            needRes = True
        elif msg == b"coordinate":
            res = move_window()
            needRes = True
        return (needRes, str.encode(res))
    
    def run(self):
        sock = socket.socket()
        sock.bind(('', self.port))
        sock.listen(1)
        conn, addr = sock.accept()
        while True:
            data = conn.recv(1024)
            if data:
                toRes, res = self.messageHandler(data)
                if toRes:
                    conn.send(res)
        conn.close()

# Запуск двух серверов в отдельных потоках
server1 = Server(9091)
server2 = Server(9092)
server1.start()
server2.start()