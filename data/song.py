from dataclasses import dataclass
from data.enums import Source

@dataclass
class Song:
    song_name: str
    artist_name: str
    duration_in_s: float
    source: Source
    reference_from_source: str

