const { Appwrite } = require("appwrite");

// Initialize Appwrite client
const appwrite = new Appwrite();

appwrite
  .setEndpoint("https://cloud.appwrite.io/v1")
  .setProject("envhub")
  .setKey(
    "658ee3ae6bf33c40348e1068bf0ee92773b07eb5f2b53152232e1434ea563b5b0d2bb799f911db728e51f2557e7efb16b9f971a2ae9df90f3a2f042e746203aa8c6776b6420c4f91315a95bfa565ebc13c56d283cefa51a11882d09cbcd1849f532b8a5cdebebc35fec980baa9c1a2ed33a0d5c82cbf68b40539b2a6b9b457a4"
  );

// Initialize Appwrite database
const database = new Appwrite.Database(appwrite);
const collectionId = "key-value-pairs";

// Serverless function handler
exports.handler = (req, res) => {
  
  const varName = req.query.varName; // Extract varName from URL

  // List documents to find a document with ID matching varName
  database
    .listDocuments(collectionId, [], varName)
    .then((response) => {
      const document = response.documents[0];

      if (document) {
        const value = document.fields.value;
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ varName, value }));
      } else {
        res.writeHead(404, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Variable not found" }));
      }
    })
    .catch((error) => {
      console.error(error);
      res.writeHead(500, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Internal Server Error" }));
    });
};
