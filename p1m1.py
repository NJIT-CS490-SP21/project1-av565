import os
import requests
import time
import dotenv
import random
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
    global dotenv_file
    token = os.getenv("TOKEN")
    if t - float(os.getenv("TOKEN_TIMEOUT")) >= 3600:
        token = get_new_access_token()
        dotenv.set_key(dotenv_file, "TOKEN", token)
        dotenv.set_key(dotenv_file, "TOKEN_TIMEOUT", str(time.time()))
        print("Creating a new token")
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)
    return token


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


def p1m1_main():
    artists_id = ["1mYsTxnqsietFxj1OgoGbG", "5mqguTgtaoCMNMZD6txCh6", "0gxyHStUsqpMadRV0Di1Qt"]

    artist_num = random.randint(0, len(artists_id) - 1)
    top_tracks = get_top_song_of_artist(artists_id[artist_num])

    song_num = random.randint(0, len(top_tracks) - 1)
    song = top_tracks[song_num]

    # print(js.dumps(song, indent=4, sort_keys=True))
    # print(song["preview_url"])
    song = {
        "name": song["name"],
        "song_url": song["external_urls"]["spotify"],
        "artists": [artist["name"] for artist in song["artists"]],
        "artist_links": [artist["external_urls"]["spotify"] for artist in song["artists"]],
        "image_url": song["album"]["images"][0]["url"],
        "album_name": song["album"]["name"],
        "album_release_date": song["album"]["release_date"],
        "length": song["duration_ms"],
        "song_preview": song["preview_url"] if (song["preview_url"] != "null") else None
    }
    return song
# print("------------------------------------------")
# print(js.dumps(song, indent=4))
