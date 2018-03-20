from http.server import BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length'))
        content_type = self.headers.get('Content-Type')
        print(content_type)
        word_frames = self.rfile.read(content_length)
        print(word_frames)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

