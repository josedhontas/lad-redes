import socket

def start_server():
    host = 'localhost'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(1)
    print("Servidor esta ouvindo em {}:{}".format(host, port))

    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexao estabelecida com {}".format(client_address))

        request = client_socket.recv(4096)
        print("Solicitacao do cliente:")
        print(request)

        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<html><body><h1>Servidor Python</h1><p>Esta e uma resposta do servidor de exemplo.</p></body></html>"
        client_socket.sendall(response)

        client_socket.close()

if __name__ == "__main__":
    start_server()
