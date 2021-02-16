import os
import dotenv
import random
import requests

dotenv.load_dotenv(dotenv.find_dotenv())
sptify_id = os.getenv("SPOTIFY_ID")
spotify_secret = os.getenv("SPOTIFY_SECRET")
spotify_base_url = "https://api.spotify.com/v1/"


def get_new_spotify_token():
    authentication_url = "https://accounts.spotify.com/api/token"

    params = {
        "grant_type": "client_credentials",
        "client_id": sptify_id,
        "client_secret": spotify_secret
    }

    authentication_response = requests.post(authentication_url, params)

    try:
        return authentication_response.json()["access_token"]
    except:
        return None


access_token = get_new_spotify_token()
headers = {"Authorization": "Bearer {}".format(access_token)}


def get_top_song_of_artist(artist_id):
    '''
    return: list of all top song json objects
    '''
    if access_token == None:
        return None
    url = spotify_base_url + "artists/{}/top-tracks".format(artist_id)
    params = {"id": artist_id, "market": "US"}
    response = requests.get(url=url, headers=headers, params=params)
    data = response.json()
    try:
        return data["tracks"]
    except:
        return None
