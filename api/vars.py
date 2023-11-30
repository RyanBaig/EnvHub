from appwrite.client import Client
from appwrite.services.databases import Databases

client = Client()

(client
  .set_endpoint('https://cloud.appwrite.io/v1') # Your API Endpoint
  .set_project('envhub') # Your project ID
  .set_key('658ee3ae6bf33c40348e1068bf0ee92773b07eb5f2b53152232e1434ea563b5b0d2bb799f911db728e51f2557e7efb16b9f971a2ae9df90f3a2f042e746203aa8c6776b6420c4f91315a95bfa565ebc13c56d283cefa51a11882d09cbcd1849f532b8a5cdebebc35fec980baa9c1a2ed33a0d5c82cbf68b40539b2a6b9b457a4') # Your secret API key
)

db_id = "env_vars"
collection_id = "key-value-pairs"

def handler(req):
    doc_id = req.query.get("varName", "")
    if not doc_id:
        return {"statusCode": 400, "body": "varName parameter is required"}

    database = Databases(client)

    try:
        result = database.get_document(db_id, collection_id, doc_id)
        return {"statusCode": 200, "value": result}
    except Exception as e:
        return {"statusCode": 500, "value": str(e)}