const fetch = require("node-fetch");

const token = "QUhi52tmDlQBhj39M0Ug3tLo";

// Function to fetch the vars from Vercel API
const fetchVarsFromVercel = async () => {
  const response = await fetch(
    "https://api.vercel.com/v1/projects/EnvHub/env",
    {
      method: "GET",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    throw new Error(
      `Error fetching vars from Vercel API: ${response.statusText}`
    );
  }

  return response.json();
};

module.exports = async (req, res) => {
  const url = new URL(req.url, `https://${req.headers.host}`);
  const varName = url.pathname.substring(1);

  if (varName === "VERCEL_AUTH_TOKEN_FOR_ENV_HUB") {
    res.status(404).json({ msg: "Variable not found", status: 404 });
    return;
  }

  try {
    const varsFromVercel = await fetchVarsFromVercel();
    const matchedVar = varsFromVercel.find((envVar) => envVar.key === varName);

    if (matchedVar) {
      res.status(200).json({ value: matchedVar.value });
    } else {
      res.status(404).json({ msg: "Variable not found", status: 404 });
    }
  } catch (error) {
    console.error("Error retrieving vars:", error);
    res
      .status(500)
      .json({ msg: "Error Retrieving vars for Database", status: 500 });
  }
};
