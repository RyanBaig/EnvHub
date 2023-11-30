from appwrite.client import Client
from appwrite.services.databases import Databases
from http.server import BaseHTTPRequestHandler
import json

client = Client()

client.set_endpoint('https://cloud.appwrite.io/v1')
client.set_project('envhub')
client.set_key('658ee3ae6bf33c40348e1068bf0ee92773b07eb5f2b53152232e1434ea563b5b0d2bb799f911db728e51f2557e7efb16b9f971a2ae9df90f3a2f042e746203aa8c6776b6420c4f91315a95bfa565ebc13c56d283cefa51a11882d09cbcd1849f532b8a5cdebebc35fec980baa9c1a2ed33a0d5c82cbf68b40539b2a6b9b457a4')

db_id = "env_vars"
collection_id = "key-value-pair"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self, event=None, context=None):
        try:
            # Split the path into parts
            path_parts = self.path.split('/')

            # Extract the variable name from the path
            var_name = path_parts[-1] if len(path_parts) > 1 else None

            if not var_name:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"message": "Varname parameter is required"}')
                return

            doc_id = var_name

            if not doc_id:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'{"message": "varName parameter is required"}')
                return

            database = Databases(client)

            
            try:
                result = database.get_document(db_id, collection_id, doc_id)
                print("Result:", result)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'statusCode': 200, 'value': result.get("value", "")}
                self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                print("Error:", e)
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {'statusCode': 500, 'errors': str(e)}
                self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = '{"statusCode": 400, "error": "' + str(e) + '"}'
            self.wfile.write(response.encode())


# This part is needed for local testing, it won't be executed when deployed on Vercel
# if __name__ == '__main__':
#     from http.server import HTTPServer

#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, MyHandler)
#     print('Starting server...')
#     httpd.serve_forever()
