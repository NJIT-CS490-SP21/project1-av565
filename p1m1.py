import os
import requests
import time
import dotenv
import json as js

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_new_access_token():
    authentication_url = "https://accounts.spotify.com/api/token"

    params = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    authentication_response = requests.post(authentication_url, params)
    access_token = authentication_response.json()["access_token"]
    return access_token


def create_access_token(t=time.time()):
    if t - float(os.getenv("TOKEN_TIMEOUT")) >= 3600:
        dotenv.set_key(dotenv_file, "TOKEN", get_new_access_token())
        dotenv.set_key(dotenv_file, "TOKEN_TIMEOUT", str(time.time()))
        print("Creating a new token")
    dotenv.load_dotenv(dotenv_file)
    return str(os.getenv("TOKEN"))


access_token = create_access_token()

base_url = "https://api.spotify.com/v1/"

headers = {"Authorization": "Bearer {}".format(access_token)}


# def get_artist_id(artist_name, market = "US"):
#     url = base_url + "search"
#     params = {'q': artist_name, "type": "artist", "market": market, "limit": 100, "offset": 0}


def get_top_song_of_artist(artist_id):
    '''
    return: list of all top song json objects
    '''
    url = base_url + "artists/{}/top-tracks".format(artist_id)
    params = {"id": artist_id, "market": "US"}
    response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    return data["tracks"]


# url = base_url + "browse/new-releases"

# number_of_songs = 10
# params = {"country": "US", "limit": number_of_songs, "offset": 0}

# response = requests.get(url=url, headers=headers, params=params)

# data = response.json()
# for i in range(number_of_songs):
#     print(data["albums"]["items"][i]["name"])

# url = base_url + "playlists/37i9dQZEVXbMDoHDwVN2tF"
# params = {'q': "Global Top 50", "type": "playlist"}
# response = requests.get(url=url, headers=headers)

# data = response.json()
# for track in data["tracks"]["items"]:
#     artists = [artist["name"] for artist in track["track"]["album"]["artists"]]
#     out_string = "{} BY: {}".format(track["track"]["album"]["name"], ", ".join(artists))
#     print(out_string)
# print(data["tracks"]["items"][4]["track"]["album"])

# print(js.dumps(data, indent=4, sort_keys=True))

artists_id = ["1mYsTxnqsietFxj1OgoGbG", "5mqguTgtaoCMNMZD6txCh6", "0gxyHStUsqpMadRV0Di1Qt"]
print(get_top_song_of_artist(artists_id[1])[0]["name"])
