import time
import os

from pyfiglet import Figlet

from services.spotifyservice import SpotifyService
from ytmusicapi import YTMusic


def main():
    print("Hello World, thats the initial commit")
    # time.sleep(3)
    # f = Figlet(font='slant')
    # print(f.renderText(f'Spotify to YouTube Music'))
    spotify = SpotifyService()
    #songs = spotify.getSongsByKeyword("u2", 3)
    #for x in songs:
    #    print(x)
    playlist = spotify.getSongsInPlaylistById("3guAfgfqBXolcknhXwNSeT", "TestName")
    for x in playlist.songs:
        print(x)


if __name__ == "__main__":
    main()
