import os
import requests
import time
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)


def get_new_access_token():
    authentication_url = "https://accounts.spotify.com/api/token"

    params = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("CLIENT_ID"),
        "client_secret": os.getenv("CLIENT_SECRET")
    }

    authentication_response = requests.post(authentication_url, params)
    access_token = authentication_response.json().authentication_response_data["access_token"]
    return access_token


def create_access_token(t=time.time()):
    if t - float(os.getenv("TOKEN_TIMEOUT")) >= 3600:
        dotenv.set_key(dotenv_file, "TOKEN", get_new_access_token())
        dotenv.set_key(dotenv_file, "TOKEN_TIMEOUT", str(time.time()))
    dotenv.load_dotenv(dotenv_file)
    return str(os.getenv("TOKEN"))


access_token = create_access_token()

base_url = "https://api.spotify.com/v1/"

headers = {"Authorization": "Bearer {}".format(access_token)}

url = base_url + "browse/new-releases"

number_of_songs = 10
params = {"country": "US", "limit": number_of_songs, "offset": 0}

response = requests.get(url=url, headers=headers, params=params)

data = response.json()
for i in range(number_of_songs):
    print(data['albums']['items'][i]['name'])

print("Hello world this worked")
