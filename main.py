from http.server import SimpleHTTPRequestHandler
import socketserver
import os

# On définit le port (8080 est standard pour le web)
PORT = int(os.environ.get("PORT", 8080))

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Si on demande la racine, on donne l'index.html
        if self.path == '/':
            self.path = 'index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

print(f"Serveur lancé sur le port {PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
