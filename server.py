from http.server import HTTPServer, BaseHTTPRequestHandler

# HTML da página da Empresa Exemplo
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Empresa Exemplo</title>
</head>
<body>
    <h1>Bem-vindo à Empresa Exemplo</h1>
    <p>Descrição da empresa...</p>
</body>
</html>
"""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Servidor rodando em http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
