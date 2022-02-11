import enum

class Source(enum.Enum):
    SPOTIFY = 1
    YOUTUBE_MUSIC = 2
    OTHER = 3

    def __str__(self):
        return str(self.name)

