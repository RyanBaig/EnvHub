const express = require('express');
const router = express.Router();
const token = process.env.VERCEL_AUTH_TOKEN_FOR_ENV_HUB;

// function to fetch the vars from Vercel API
const fetchVarsFromVercel = async () => {
  // Make a request to the Vercel API to get the environment vars
  const response = await fetch(
    "https://api.vercel.com/v1/projects/EnvHub/env",
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );
  const data = await response.json();

  // Put all the environment vars in an iterable
  const environmentVars = Object.entries(data).map(([key, value]) => ({
    key,
    value,
  }));

  return environmentVars;
};

router.get('/:varName', async (req, res) => {
  const varName = req.params.varName;
  console.log("YAHOOO")
  if (varName === "VERCEL_AUTH_TOKEN_FOR_ENV_HUB") {
    res.status(404).send({ msg: "Variable not found", status: 404 });
    return;
  }
  
  try {
    const varsFromVercel = await fetchVarsFromVercel();
    const matchedVar = varsFromVercel.find((envVar) => envVar.key === varName);

    if (matchedVar) {
      res.send({ value: matchedVar.value });
    } else {
      res.status(404).send({ msg: 'Variable not found', status: 404 });
    }
  } catch (error) {
    console.error('Error retrieving vars:', error);
    res.status(500).send({ msg: 'Error Retrieving vars for Database', status: 500 });
  }
});