import time
import os

from pyfiglet import Figlet

from services.spotifyservice import SpotifyService


def main():
    print("Hello World, thats the initial commit")
    #time.sleep(3)
    #f = Figlet(font='slant')
    #print(f.renderText(f'Spotify to YouTube Music'))
    spotify = SpotifyService()
    songs = spotify.getSongsByKeyword("u2", 3)
    playlist = spotify.getSongsInPlaylistById("3guAfgfqBXolcknhXwNSeT")
    print(playlist)
    #print(songs)


if __name__ == "__main__":
    main()