from dataclasses import dataclass


@dataclass
class Song:
    song_name: str
    artist_name: str
    duration_in_s: float
    source: str
    reference_from_source: str

