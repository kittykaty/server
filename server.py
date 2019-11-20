import socket

HOST, PORT = '0.0.0.0', 80 #config of host and port

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #first socket that uses IPv4 and second that use TCP
my_socket.setsockport(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind((HOST, PORT)) # set addresses and port for socket
my_socket.listen(1) #set socket to hear request from 1 client max

print('Сервер відкритий на порту: ', PORT)

while True:
    print("Очікую підключення...")
    connection, address = my_socket.accept()
    request = connection.recv(1024).decode('utf-8') #info. of request

    string_list = request.split(' ')
    method = string_list[0]

    requesting_file = string_list[1]

    print('Запит клієнта ', requesting_file)

    myfile = requesting_file.split()[0]
    myfile = myfile.lstrip('/')
    if (myfile == ''):
        myfile = 'index.html'
    try:
        file = open(myfile, 'rb')
        response = file.read()
        file.close()

        header = 'HTTP/1.1 200 OK\n'

        if (myfile.endswith(".jpg")):
            mimetype = 'image/jpg'
        elif (myfile.endswith(".css")):
            mimetype = ' code/css'
        else:
            mimetype = 'code/html'

        header += 'Content-Type: ' +str(mimetype) + '\n\n'

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</center></body></html>'
            'utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    connection.send(final_response)
    connection.close()
