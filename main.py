from services.spotifyservice import SpotifyService
from ytmusicapi import YTMusic

from services.youtubemusicservice import YouTubeMusicService


def main():
    print("Hello World, thats the initial commit")
    # time.sleep(3)
    # f = Figlet(font='slant')
    # print(f.renderText(f'Spotify to YouTube Music'))
    spotify = SpotifyService()
    #songs = spotify.getSongsByKeyword("u2", 3)
    #for x in songs:
    #    print(x)
    youtube = YouTubeMusicService()
    playlist = spotify.getSongsInPlaylistById("3guAfgfqBXolcknhXwNSeT", "TestName")
    for song in playlist.songs:
        ytSong = youtube.getIdByName(song.song_name)
        # TODO Filter search response for type, e.g. only songs, not artists
        if isinstance(ytSong[0], dict):
            print(ytSong[0]['videoId'])
        else:
            print(f'Not a Song{ytSong}')


if __name__ == "__main__":
    main()
