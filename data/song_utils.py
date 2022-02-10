from dataclasses import dataclass

from data.enums import Source


@dataclass
class Song:
    song_name: str
    artist_name: str
    duration_in_s: float
    source: Source
    reference_from_source: str

    def __str__(self):
        return f'Name: {self.song_name}, Artist: {self.artist_name}, Duration: {self.duration_in_s}, Source: {self.source}, Source reference: {self.reference_from_source}'


@dataclass
class Playlist:
    name: str
    songs: list[Song]

    def __init__(self, playlistName):
        self.name = playlistName
        self.songs = []
