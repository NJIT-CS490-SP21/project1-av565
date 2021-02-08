CS490 Project 1 Milestone 1
    This [temporary] app shows information on a random artist's top played song, from a list of three hard-coded artists.
    PLEASE NOTE:
        The song returned *might not* be the top song by listned to. This is just a random song from Spotify API's https://api.spotify.com/v1/artists/{id}/top-tracks GET request.

PACKAGES USED (SOME MAY HAVE ALREADY BEEN INSTALLED):
    1. Flask: install using command: pip install -U "python-dotenv"
    2. requests: install using command: python -m pip install requests
    3. os
    4. time
    5. dotenv
    6. random

BEFORE SET-UP:
    1. Make sure you have Python installed (latest version is preffered).
    2. Create a Spotify account/log-in here: https://developer.spotify.com/dashboard/
    3. Create a new app. Look here for reference/help: https://developer.spotify.com/documentation/web-api/quick-start/ https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app
    4. Open up the app to look a the information. Proceed to "HOW TO SET-UP"

HOW TO SET-UP:
    1. Make a .env file in the same directory as the app.py, and p1m1.py. Put YOUR OWN client_id and client_secret from Spotify. Make sure the file follows the format:
            CLIENT_ID="<your-id>"
            CLIENT_SECRET="<your-secret>"
    2. Make sure you have all the required packages installed, along with Python (latest version would be good).
    3. Run app.py
    4. Go to "localhost:8080" on your browser.

MS1 Questions:
    a. 
        1. I was unable to send the song's json dictionary to the flask template. I created my own dictionary to store the essential information from the song.json() object, and sent that instead.
        2. I had trouble properly making the song preview player. I looked at the right website (the one from firefox) and figured out somehow.
        3. I had a lot of trouble trying to stylize my app. Ended up with a bare website that doesn't look too good, but meets the minimum requirements for the first Milestone.
    b. There are 2 problems. Sometimes the key and secrets wont load properly, and result in not giving a working access_token. The only solution I found was re-running app.py. I also couldn't properly stylize the elements the way I wanted.
    c. Definitely fix the access_token problem. Definitely do my best to stylize the page so it doesn't look like something from the Dark Ages.
