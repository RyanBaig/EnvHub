from http.server import BaseHTTPRequestHandler
from appwrite.exception import AppwriteException
from appwrite.client import Client
from appwrite.services.databases import Databases
import json
import logging

logging.basicConfig(level=logging.INFO)

client = Client()

(client
    .set_endpoint('https://cloud.appwrite.io/v1')
    .set_project('envhub')
    .set_key('658ee3ae6bf33c40348e1068bf0ee92773b07eb5f2b53152232e1434ea563b5b0d2bb799f911db728e51f2557e7efb16b9f971a2ae9df90f3a2f042e746203aa8c6776b6420c4f91315a95bfa565ebc13c56d283cefa51a11882d09cbcd1849f532b8a5cdebebc35fec980baa9c1a2ed33a0d5c82cbf68b40539b2a6b9b457a4')
)

db_id = "env_vars"
collection_id = "key-value-pair"

database = Databases(client)

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get the varname and varvalue from request body
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            data = json.loads(body.decode('utf-8'))

            var_name = data.get('varName', '')
            var_value = data.get('varValue', '')

            if not var_name or not var_value:
                self.send_error_response(400, "'varName' and 'varValue' parameters are required. Make sure they are present and try again.")

            try:
                # Check if the same varname already exists in the database
                result = database.get_document(db_id, collection_id, var_name)

                # If it exists, send a 409 response
                self.send_error_response(409, 'varName already exists. Please use a different name and Try again.')

            except AppwriteException as e:
                # If an exception is raised by get_document, it means varname does not exist, proceed to create
                try:
                    database.create_document(db_id, collection_id, var_name, json.dumps({"key": var_name, "value": var_value}))
                    self.send_success_response(200, 'Variable added to the database successfully.', {'varName': var_name, 'varValue': var_value})

                except AppwriteException as e:
                    # Handle AppwriteException when creating a new document
                    self.send_error_response(600, str(e))

        except Exception as e:
            # Handle other exceptions
            self.send_error_response(500, str(e))
            logging.exception('Internal Server Error')

    def send_error_response(self, status_code, error_message):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'statusCode': status_code, 'error': error_message}).encode('utf-8'))

    def send_success_response(self, status_code, message, data=None):
        response = {'statusCode': status_code, 'message': message}
        if data:
            response.update(data)

        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))


# if __name__ == '__main__':
#     from http.server import HTTPServer
#     server = HTTPServer(('localhost', 8000), MyHandler)
#     print('Starting server on http://localhost:8000')
#     server.serve_forever()
