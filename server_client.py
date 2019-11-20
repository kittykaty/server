import socket
impot argparse

def Main():
    parser = argparse.ArgumentParser(description = "Хост і порт")
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
    s.connect((host,port))

    print("Сокет під'єднаний")
    while 1:
        message = input (" Введіть повідомлення, що треба передати серверу: \n")
        try:
            s.sendall(message.encode())
        except socket.error:
            print("Повідомлення не відправлено")
            break

        print("Повідомлення успішно відправлене.\n")

        reply = s.recv(1024)
        print(reply.decode())
    s.close()

if __name__ == '__main__':
    Main()
