import socket
import argparse
from _thread import *

#thread fucnttion
def client_thread(conn):
    message = "Успішне з'єднання з сервером.\n"
    conn.send(message.encode())
    while True:
        data = conn.recv(1024) #data fom client
        reply = "Отримані від клієнта дані: {0} ".format(data.decode())
        if not data:
            break
        conn.send(reply.encode())

    conn.close()

def Main():
    parser = argparse.ArgumentParser(description= "Хост і порт")
    parser.add_argument('--host', dest="host", required=False)
    parser.add_argument('--port', dest="port", type=int, required=True)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port

    if not host:
        host = "127.0.0.1"
    if not port:
        port = "8080"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    print("Сокет прив'язаний до порта:", port)

    s.listen(5)
    pint("Сокет чекає на з'єднання")

    while True:
        conn, addr = s.accept()

        print("Клієнт під'єднаний до: {0} : {1}".format(addr[0], addr[1]))

        start_new_thread(client_thread, (conn,))
    s.close()
