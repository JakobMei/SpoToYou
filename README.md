# SpoToYou
This application can convert a ==Music-Playlist== from Spotify to a YouTube-Music Playlist, as there is no official service for that. Therefore it loops over the Spotify-Playlist, searches for each song on YouTube-Music and adds the song to a new or already existing playlist.

# used Packages sofar
 - pyfiglet for fancy console text
 - dotenv for environment variables
 - spotipy as spotify api/sdk
 - ytmusicapi as api/sdk for youtube music

# Prerequisites
##1.  Installation & virtual Environment

Create virtual environment and install all the needed packages from requirements.txt as follows:

```
    python -m venv ./venv
```

```
    venv\bin\activate
```

```
    pip install -r requirements.txt
```
##2. Environment Variables for Spotify
file for env vars needs to be created, currently named "variables.txt".
currently follows this structure:
```
CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CLIENT_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
 ```
*secret & id are for spotify authentication and can be created at [Spotify Developer Portal](https://developer.spotify.com/dashboard/applications)*
##3. Authentication Header for YT-Music
file for YT music authentication needs to be created in /services called "headers_auth.json".
currently follows this structure:
```
{
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json",
    "X-Goog-AuthUser": "0",
    "x-origin": "https://music.youtube.com",
    "Cookie" : "paste your own cookie here"
}
```
[click here to learn more about how to get your own YTMusic Cookies](https://ytmusicapi.readthedocs.io/en/latest/setup.html#manual-file-creation)


