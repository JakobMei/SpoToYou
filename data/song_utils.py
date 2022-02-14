from dataclasses import dataclass

from data.enums import Source


@dataclass
class Song:
    song_name: str
    artist_name: str
    duration_in_s: float
    source: Source
    spotify_id: str
    ytmusic_id: str

    def __str__(self):
        return f'Name: {self.song_name}, Artist: {self.artist_name}, Duration: {self.duration_in_s}, Source: {self.source}'

    def __str_long__(self):
        return f'Name: {self.song_name}, Artist: {self.artist_name}, Duration: {self.duration_in_s}, Source: {self.source}, Source reference: {self.spotify_id}'


@dataclass
class Playlist:
    name: str
    songs: list[Song]
    spotify_id: str
    ytmusic_id: str
    playlist_description: str

    def __init__(self, playlistName, spotify_id, ytmusic_id, playlist_description):
        self.name = playlistName
        self.songs = []
        self.spotify_id = spotify_id
        self.ytmusic_id = ytmusic_id
        self.playlist_description = playlist_description

    def __str__(self):
        song_repr = ""
        for s in self.songs:
            song_repr = song_repr + s.__str__() + "\n"
        return f'Playlist Name: {self.name}, Songs:\n {song_repr}'
