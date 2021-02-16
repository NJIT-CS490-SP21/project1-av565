import os
import dotenv
import random
import requests
import json as js
from collections import Counter

dotenv.load_dotenv(dotenv.find_dotenv())
genius_token = os.getenv("GENIUS_TOKEN")
genius_base_url = "https://api.genius.com/"


def detox(song_name):
    try:
        start_position = song_name.index("(feat")
        end_position = song_name.index(')', start_position)
        clean_song = song_name[:start_position - 1] + song_name[end_position + 1:]
        return clean_song
    except ValueError:
        return song_name


def string_difference(original, comparer):
    '''
    returns maximum difference (in percentage) between two strings
    '''
    original = original.replace(' ', '').lower()
    comparer = comparer.replace(' ', '').lower()
    common_letters = Counter(original) & Counter(comparer)
    common_letter_count = sum(common_letters.values())
    print(original, comparer)
    return (abs(common_letter_count - len(original)) / len(original)) * 100


def genius_search_for_song(song_name):
    search_url = genius_base_url + "search"
    headers = {"Authorization": "Bearer {}".format(genius_token)}
    params = {
        'q': detox(song_name)
    }
    response = requests.get(search_url, data=params, headers=headers)
    data = response.json()

    try:
        return [s for s in data["response"]["hits"] if s["type"] == "song"][0]
    except:
        return None


def genius_search_for_artist(artist_name, closeness):
    search_url = genius_base_url + "search"
    headers = {"Authorization": "Bearer {}".format(genius_token)}
    params = {
        'q': artist_name
    }
    response = requests.get(search_url, data=params, headers=headers)
    data = response.json()
    # print(js.dumps(data, indent=2))
    try:
        return [[s["result"]["primary_artist"]["name"], s["result"]["primary_artist"]] for s in data["response"]["hits"] if string_difference(s["result"]["primary_artist"]["name"], artist_name) >= 80][0]
    except:
        return None
