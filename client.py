import socket

def test_server():
    print("Passos para testar o servidor web:")
    print("1. Certifique-se de que o servidor está em execução.")
    print("2. Abra um navegador da web e acesse: http://localhost:8080/")
    print("3. Verifique se a página da Empresa Exemplo é exibida corretamente.")
    print("\nTeste automatizado:")
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
        print(f"Status da resposta: {data.splitlines()[0]}")
        print("Conteudo da pagina:")
        print(data)
    except ConnectionRefusedError:
        print("Erro: Nao foi possivel conectar ao servidor. Certifique-se de que o servidor esta em execucao.")
    finally:
        conn.close()

if __name__ == "__main__":
    test_server()
