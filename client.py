import http.client

def test_server():
    print("Passos para testar o servidor web:")
    print("1. Certifique-se de que o servidor está em execução (execute 'python server.py').")
    print("2. Abra um navegador da web e acesse: http://localhost:8080/")
    print("3. Verifique se a página da Empresa Exemplo é exibida corretamente.")
    print("\nTeste automatizado:")
    try:
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/")
        response = conn.getresponse()
        data = response.read().decode()
        print(f"Status da requisição: {response.status}")
        print("Conteúdo da página:")
        print(data)
    except ConnectionRefusedError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que o servidor está em execução.")

if __name__ == "__main__":
    test_server()
