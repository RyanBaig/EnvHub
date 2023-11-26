const { Client } = require("appwrite");

// Initialize Appwrite client
const appwrite = new Client();

appwrite
  .setEndpoint("https://cloud.appwrite.io/v1")
  .setProject("envhub");

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
