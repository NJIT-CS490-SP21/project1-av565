# CS490 Project 1

    This app shows information on a random artist's top played song, from a list of nine hard-coded artists. Furthermore, the app fetches a Genius lyrics link to the song (closest), and if the song is not available, it attempts to fetch the [primary artist]'s link on Genius.
    The song image and the name of the song takes you to the song on spotify.
    The artists' names take you to the corresponding page on Spotify.
    The "Genius Lyrics" takes you to the lyrics page from Genius.
    PLEASE NOTE:
        The song returned *might not* be the top song by listned to. This is just a random song from Spotify API's https://api.spotify.com/v1/artists/{id}/top-tracks GET request.

## PACKAGES/LIBRARIES USED (SOME MAY HAVE ALREADY BEEN INSTALLED):

    1. Flask: install using command: pip install -U "python-dotenv"
    2. requests: install using command: python -m pip install requests
    // Others SHOULD be part of python
    3. os
    5. dotenv
    6. random
    7. collections

## BEFORE SET-UP:

    1. Make sure you have Python installed (latest version is preffered).
    2. Create a Spotify account/log-in here: https://developer.spotify.com/dashboard/
    3. Create a new app. Look here for reference/help: https://developer.spotify.com/documentation/web-api/quick-start/ https://developer.spotify.com/documentation/general/guides/app-settings/#register-your-app
    5. Create a Genius account/log-in here: https://genius.com/api-clients Look here for reference: https://docs.genius.com/
    6. Go back to https://genius.com/api-clients and create a new app (following the instructions in https://docs.genius.com/)
    4. Open up both apps (Spotify and Genius) to look at the information. On the Genius App, click on "Generate Access Token" to generate a new token. Keep the apps open and proceed to next step.
    5. Proceed to "HOW TO SET-UP"

## HOW TO SET-UP:

    1. Make a .env file in the same directory as the app.py, and p1m1.py. Put YOUR OWN client_id and client_secret from Spotify. Make sure the file follows the format:
            SPOTIFY_ID="[your-spotify-id]"
            SPOTIFY_SECRET="[your-spotify-secret]"
            GENIUS_TOKEN="[your-genius-token]"
    where [your-spotif-id], [your-spotify-secret] are your spotify app's id and secrets, and [your-genius-token] is the genius token you got from clicking the Generate Access Token button.
    2. Make sure you have all the required packages installed, along with Python (latest version would be good).
    3. Run app.py
    4. Go to "localhost:8080" on your browser.
    5. If you're lazy, just visit https://av565-project-1.herokuapp.com/

## MS1 AND MS2 COMBINED:

    a.
        1. I was unable to send the song's json dictionary to the flask template. I created my own dictionary to store the essential information from the song.json() object, and sent that instead.
        2. Had trouble figuring out the Genius auth flow, found out that you do not need to generate an access token everytime.
        3. Had issues with stylizing, somehow figured out a way to center the song info according to the song image. I used a display: flex CSS for the image, making it the size of the entire page (hopefully)
    b. The only issue is how the genius API works. I wanted to generate an artist link incase the song is not found, but as it might turn out, there is no way for the song to *NOT* be available.
    c. Make the Page a bit more stylized, formatting and centering the elements correctly.
    d. In the future, I would change up the stylizing, make it according to my *dream* look. I would also add user interactivity by making the artists chosen by the user. Some other feature might be using web-scraping to display the lyrics on the page, and making something on the page to change according to the frequency of the song from the <audio> element.
