import time
import os
from dotenv import load_dotenv

from pyfiglet import Figlet

from services.spotifyservice import SpotifyService


def main():
    load_dotenv()
    print("Hello World, thats the initial commit")
    time.sleep(3)
    f = Figlet(font='slant')
    print(f.renderText(f'Spotify to YouTube Music'))
    spotify = SpotifyService()
    spotify.search("u2")


if __name__ == "__main__":
    main()