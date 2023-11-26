// Implement a way to get all the environment vars from the Vercel API and then
// put them all in an iterable
// see if the value of parameter in the url of this func is equal to any of the environment vars
// if it does, return the value associated with the var

// Implement a function to get all the environment vars from the Vercel API
async function getEnvironmentVars() {
    // Make a request to the Vercel API to get the environment vars
    const response = await fetch('https://api.vercel.com/v1/projects/EnvHub/env');
    const data = await response.json();

    // Put all the environment vars in an iterable
    const environmentVars = Object.entries(data).map(([key, value]) => ({ key, value }));

    return environmentVars;
}

// Implement a function to check if the value of a parameter in the URL is equal to any of the environment vars
function checkParameterValue(parameter, environmentVars) {
    const matchedVar = environmentVars.find((envVar) => envVar.value === parameter);

    if (matchedVar) {
        return matchedVar.value;
    }

    return null;
}
