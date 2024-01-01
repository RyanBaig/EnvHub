"""
This file contains functions related to interacting with the EnvHub API.

Functions:
    get_var(name): Retrieves the value of a variable from the EnvHub API.
"""
import requests
from requests.exceptions import ConnectionError

def get_var(name: str) -> str:
    """
    Retrieves the value of a variable from the EnvHub API.
    
    Parameters:
        name (str): The name of the variable to retrieve.
    
    Returns:
        str: The value of the variable.
    
    Raises:
        ConnectionError: If the API request fails or returns an error.
    """
    r = requests.get('https://envhub.ryanbaig.vercel.app/api/vars/get?varName=' + name)
    if r.status_code == 200:
        return r.json()["value"]
    else:
        raise ConnectionError(r.json())

def set_var(name: str, value: str) -> str:
    """
    Sends a POST request to the 'https://envhub.ryanbaig.vercel.app/api/vars/set' endpoint to set a variable in the environment hub.

    Args:
        name (str): The name of the variable.
        value (str): The value of the variable.

    Returns:
        str: The new value of the variable as returned by the API.

    Raises:
        ConnectionError: If there is a connection error or if the API response indicates an error.
    """
    
    body = {
        "varName": name,
        "varValue": value,
    }

    
    r = requests.post('https://envhub.ryanbaig.vercel.app/api/vars/set', json=body)
    if r.status_code == 200 and r.json()["statusCode"] == 200:
        # I should return what in this scenario? ans: the new value
        return r.json()
    else:
        raise ConnectionError(r.json())
    
    