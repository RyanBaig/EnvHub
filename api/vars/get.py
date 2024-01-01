import json
from http.server import BaseHTTPRequestHandler
from appwrite.exception import AppwriteException
from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()

(client
    .set_endpoint('https://cloud.appwrite.io/v1')
    .set_project('envhub')
    .set_key('658ee3ae6bf33c40348e1068bf0ee92773b07eb5f2b53152232e1434ea563b5b0d2bb799f911db728e51f2557e7efb16b9f971a2ae9df90f3a2f042e746203aa8c6776b6420c4f91315a95bfa565ebc13c56d283cefa51a11882d09cbcd1849f532b8a5cdebebc35fec980baa9c1a2ed33a0d5c82cbf68b40539b2a6b9b457a4')
)

db_id = "env_vars"
collection_id = "key-value-pair"

database = Databases(client)



class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Split the path into parts
            path_parts = self.path.split('/')

            # Extract the variable name from the path
            var_name = path_parts[-1] if len(path_parts) > 1 else None
            
            varname = var_name.split('=')[1]
            if not varname:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write({"message": "Varname parameter is required"})
                return
            doc_id: str = varname

            # The global database variable is already initialized before the class
            result = database.get_document(db_id, collection_id, doc_id)

            if not doc_id:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write({"message": "varName parameter is required"})
                return

            try:
            
                    # Set the headers before sending the response code
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()

                    print("Result:", result)
                    response = {'statusCode': 200, 'value': result.get('value')}
                    self.wfile.write(json.dumps(response).encode())
            except Exception as e:
                # Set the headers before sending the response code
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()

                print("Error:", e)
                response = {
                    'statusCode': 500,
                    'errors': str(e),
                    'logging': {
                        'result': result,
                        'VarName': doc_id
                    }
                }
                self.wfile.write(json.dumps(response).encode())

        
        except AppwriteException as e:
            # Set the headers before sending the response code
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            
            response = {
                'statusCode': 404,
                'errors': str(e),
            }
            self.wfile.write(json.dumps(response).encode())

        except Exception as e:
            # Set the headers before sending the response code
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            
            
            response = {
                'statusCode': 400,
                'errors': str(e),
            }
            self.wfile.write(json.dumps(response).encode())


# This part is needed for local testing, it won't be executed when deployed on Vercel
# if __name__ == '__main__':
#     from http.server import HTTPServer
#     server_address = ('', 8000)
#     httpd = HTTPServer(server_address, handler)
#     print('Starting server...')
#     httpd.serve_forever()

