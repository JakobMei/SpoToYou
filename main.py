from pyfiglet import Figlet
import click

from data.enums import Source
from data.exceptions import NotImplementedException
from services.spotifyservice import SpotifyService
from services.youtubemusicservice import YouTubeMusicService
from colorama import init, Fore, Back

spotify = SpotifyService()
youtube = YouTubeMusicService()
init(autoreset=True)


@click.group()
def main():
    f = Figlet(font='slant')
    print(f.renderText(f'SpoToYou'))
    click.echo('Hey there!')
    testAuthentications()
    click.echo(Fore.BLUE + "Shall we start? Lets Go!")
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
@click.argument('p_id', type=str)
@click.option('--name',
              '-n',
              type=str,
              help='OPTIONAL: You can set the playlists name here, otherwise the Name from the origins playlist will be taken')
@click.option('--description',
              '-d',
              type=str,
              help='OPTIONAL: You can set the new playlists description, otherwise it will be blank')
def ytm(p_id, name=None, description=None):
    '''
    This Function will convert your Spotify Playlist into a new YouTube-Music Playlist with all its songs.
    :param pid: ID of Spotify Playlist
    :param name: OPTIONAL Name of new Playlist
    :param description: OPTIONAL Description of new Playlist
    :return: nothing
    '''
    playlist = spotify.getSongsInPlaylistById(p_id, name, description)
    youtube.createPlaylistFromLocalPlaylist(playlist)


@main.command()
@click.argument('p_id', type=str)
@click.option('--name',
              '-n',
              type=str,
              help='OPTIONAL: You can set the playlists name here, otherwise the Name from the origins playlist will be taken')
def am(p_id, name=None):
    '''
    NOT IMPLEMENTED YET - This Function will convert your Spotify Playlist to a new Apple Music Playlist
    :param p_id: to be defined
    :param name: to be defined
    :return: nothing yet
    '''
    raise NotImplementedException()
    pass


def testAuthentications():
    click.echo(Fore.YELLOW + "Testing Authentications...")
    spotify.testAuthentication()
    click.echo(Fore.GREEN + "SPOTIFY SUCCESSFULLY AUTHENTICATED")
    youtube.testAuthentication()
    click.echo(Fore.GREEN + "YOUTUBE-MUSIC SUCCESSFULLY AUTHENTICATED")
    click.echo(Fore.LIGHTGREEN_EX + "Fully Authenticated and ready to go!")


# for debugging purposes, as PyCharm Debugger doesn't work, when Program is started via CL
def manualRun():
    playlist = spotify.getSongsInPlaylistById("3guAfgfqBXolcknhXwNSeT", None, None)
    youtube.createPlaylistFromLocalPlaylist(playlist)


if __name__ == "__main__":
    # manualRun()
    main()
