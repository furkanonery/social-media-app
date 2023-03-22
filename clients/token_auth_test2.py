import requests
from pprint import pprint

# {'key': 'cd9b2e0d8d698c2af1dab8718341d0be8ab9c0b7'}
def client():


    token = 'Token cd9b2e0d8d698c2af1dab8718341d0be8ab9c0b7'

    headers = {
        'Authorization': token,
    }

    response = requests.get(
        url = 'http://127.0.0.1:8000/api/user-profiles/',
        headers=headers,
    )

    print("Status Code:",response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()