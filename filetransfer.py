import http.server
import socketserver

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as http:
    print("File Transfer Server Running on Port", PORT)
    print("Open this in your browser:  http://localhost:8000")
    http.serve_forever()
