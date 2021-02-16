import os
import dotenv
import random
import requests
import json as js

dotenv.load_dotenv(dotenv.find_dotenv())
genius_token = os.getenv("GENIUS_TOKEN")
genius_base_url = "https://api.genius.com/"


def genius_search_for_song(song_name):
    search_url = genius_base_url + "search"
    headers = {"Authorization": "Bearer {}".format(genius_token)}
    params = {
        'q': song_name
    }
    response = requests.get(search_url, data=params, headers=headers)
    data = response.json()
    song = data["response"]["hits"][0]
    print(js.dumps(song, indent=4))

genius_search_for_song("Chandelier")
