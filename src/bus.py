import requests

from src.core.config import BUS_TOKEN

# Replace with your actual token
token = "99eca3619bde43496f87a3d0aa14197945aa01c64316e40dbde7ecc9a0d95a9e"

# URL for authentication
auth_url = f"https://api.olhovivo.sptrans.com.br/v2.1/Login/Autenticar?token={BUS_TOKEN}"

# URL to get data

# Create a session to persist the authentication
session = requests.Session()


async def get_bus_info(line: str):
    print("line is", line)
    data_url = f"https://api.olhovivo.sptrans.com.br/v2.1/Linha/Buscar?termosBusca={line}"
    # Authenticate
    auth_response = session.post(auth_url)
    if auth_response.status_code == 200 and auth_response.json():
        print("Authentication successful")

        # Get the data
        data_response = session.get(data_url)
        if data_response.status_code == 200:
            data = data_response.json()
            print("Data retrieved successfully:")
            print(data)
            return data
        else:
            print("Failed to retrieve data:",
                  data_response.status_code, data_response.text)
    else:
        print("Authentication failed:",
              auth_response.status_code, auth_response.text)
        return {"data": "nada"}
