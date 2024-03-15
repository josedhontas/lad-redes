import socket

def test_server():
    print("Teste automatizado:")
    try:
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(("localhost", 8080))
        conn.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
        response = b""
        while True:
            part = conn.recv(4096)
            if not part:
                break
            response += part
        data = response.decode()
        print("Status da resposta: {0}".format(data.splitlines()[0]))
        print("Conteudo da pagina:")
        print(data)
    except socket.error as e:
        if e.errno == 111:
            print("Erro: Nao foi possivel conectar ao servidor. Certifique-se de que o servidor esta em execucao.")
        else:
            raise e
    finally:
        conn.close()

if __name__ == "__main__":
    test_server()
