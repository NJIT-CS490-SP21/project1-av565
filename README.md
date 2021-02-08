CS490 Project 1 Milestone 1
This [temporary] app shows information on a random artist's top played song, from a list of three hard-coded artists.
PLEASE NOTE:
    The song returned *might not* be the top song by listned to. This is just a random song from Spotify API's https://api.spotify.com/v1/artists/{id}/top-tracks GET request.
    
a. 
    1. I was unable to send the song's json dictionary to the flask template. I created my own dictionary to store the essential information from the song.json()          object, and sent that instead.
    2. I had trouble properly making the song preview player. I looked at the right website (the one from firefox) and figured out somehow.
    3. I had a lot of trouble trying to stylize my app. Ended up with a bare website that doesn't look too good, but meets the minimum requirements for the first          Milestone.
b. There are 2 problems. Sometimes the key and secrets wont load properly, and result in not giving a working access_token. The only solution I found was re-running app.py. I also couldn't properly stylize the elements the way I wanted.
c. Definitely fix the access_token problem. Definitely do my best to stylize the page so it doesn't look like something from the Dark Ages.
