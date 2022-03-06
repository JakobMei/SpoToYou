from pyfiglet import Figlet
import click

from data.enums import Source
from data.exceptions import PlaylistCreationException
from services.spotifyservice import SpotifyService
from services.youtubemusicservice import YouTubeMusicService


def main():
    print("Hello World, thats the initial commit")
    f = Figlet(font='slant')
    print(f.renderText(f'SpoToYou'))
    # spotify = SpotifyService()
    youtube = YouTubeMusicService()
    # playlist = spotify.getSongsInPlaylistById("3guAfgfqBXolcknhXwNSeT", "TestName")
    # e = PlaylistCreationException("test", Source.SPOTIFY, playlist)
    # raise e
    # print("to")
    # youtube.createPlaylistFromLocalPlaylist(playlist)
    # for song in playlist.songs:
    #    song_id = youtube.getIdByName(song.song_name)
    #    print(song_id)



if __name__ == "__main__":
    main()
