from spotify import *
from genius import *


def project1_main():
    # bruno mars, clean bandit, anirudh ravichander, mark ronson, tones and I, katy perry, taylor swift, pharell williams
    artists_id = ["0du5cEVh5yTK9QJze8zA0C", "6MDME20pz9RveH9rEXvrOM", "4zCH9qm4R2DADamUHMCa6O", "3hv9jJF3adDNsBSIQDqcjp",
                  "2NjfBq1NflQcKSeiDooVjY", "6jJ0s89eD6GaHleKKya26X", "06HL4z0CvFAxyc27GXpf02", "2RdwBSPQiwcmiDo9kixcl8"]

    artist_num = random.randint(0, len(artists_id) - 1)
    top_tracks = get_top_song_of_artist(artists_id[artist_num])

    song_num = random.randint(0, len(top_tracks) - 1)
    song = top_tracks[song_num]

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
