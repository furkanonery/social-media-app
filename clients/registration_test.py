import requests
from pprint import pprint

def client():
    credentials = {
        'username':'Kullanici2',
        'email':'Kullanici2@gmail.com',
        'password1':'PzxL6LR33CkpQb4',
        'password2':'PzxL6LR33CkpQb4',
    }

    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data = credentials
    )

    print("Status Code:",response.status_code)

    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()