from http.server import HTTPServer

from server.server_config import HOST, PORT
from server.request_handler import RequestHandler


# if __name__ == '__main__':
print('Enter script')
server_address = HOST, PORT
detection_server = HTTPServer(server_address, RequestHandler)
print('Detection server started on PORT {0}'.format(PORT))
try:
    detection_server.serve_forever()
except KeyboardInterrupt:
    detection_server.server_close()
    print('Detection server stopped')
