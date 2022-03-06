from pyfiglet import Figlet
import click

from data.enums import Source
from data.exceptions import PlaylistCreationException
from services.spotifyservice import SpotifyService
from services.youtubemusicservice import YouTubeMusicService

spotify = SpotifyService()
youtube = YouTubeMusicService()


@click.group()
def main():
    f = Figlet(font='slant')
    print(f.renderText(f'SpoToYou'))
    click.echo('Hey there!')
    pass

    # playlist = spotify.getSongsInPlaylistById("3guAfgfqBXolcknhXwNSeT", None)
    # print("test")
    # e = PlaylistCreationException("test", Source.SPOTIFY, playlist)
    # raise e
    # print("to")
    # youtube.createPlaylistFromLocalPlaylist(playlist)
    # for song in playlist.songs:
    #    song_id = youtube.getIdByName(song.song_name)
    #    print(song_id)


@main.command()
@click.argument('id', type=str)
@click.option('--name',
              '-n',
              type=str,
              help='OPTIONAL: You can set the playlists name here, otherwise the Name from the origins playlist will be taken')
@click.option('--description',
              '-d',
              type=str,
              help='OPTIONAL: You can set the new playlists description, otherwise it will be blank')
def ytm(id, name=None, description=None):
    '''
    This Function will convert your Spotify Playlist into a new YouTube-Music Playlist with all its songs.
    :param playlistId: ID of Spotify Playlist
    :param name: OPTIONAL Name of new Playlist
    :param description: OPTIONAL Description of new Playlist
    :return: success or failure
    '''
    playlist = spotify.getSongsInPlaylistById(id, name, description)
    youtube.createPlaylistFromLocalPlaylist(playlist)


@main.command()
def am(playlistId, playlistName=None):
    '''
    NOT IMPLEMENTED YET - This Function will convert your Spotify Playlist to a new Apple Music Playlist
    :param playlistId: to be defined
    :param playlistName: to be defined
    :return: nothing yet
    '''
    pass


if __name__ == "__main__":
    main()