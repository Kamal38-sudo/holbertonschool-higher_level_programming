from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Define server address and port
HOST = 'localhost'
PORT = 8000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Root endpoint
        if self.path == '/':
            self.send_response(200)  # HTTP status code 200 OK
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        
        # /data endpoint serving JSON
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)  # Convert dict to JSON string
            self.wfile.write(json_data.encode('utf-8'))
        
        # /status endpoint
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        # Handle undefined endpoints
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found: The requested endpoint does not exist.")

def run_server():
    server_address = (HOST, PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running at http://{HOST}:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
