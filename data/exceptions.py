class PlaylistException(Exception):
    def __init__(self, message, source, playlist):
        super().__init__(message)
        self.message = message
        self.source = source
        self.playlist = playlist


class SongException(Exception):
    def __init__(self, message, source, song):
        super().__init__(message)

        self.source = source
        self.song = song


class PlaylistCreationException(PlaylistException):
    def __init__(self, message, source, playlist):
        super().__init__(message, source, playlist)

    def __str__(self):
        return f'Error whilst creating a new Playlist at {self.source} with Playlist {self.playlist.name}. Error: {self.message}'


class AuthenticationException(Exception):
    def __init__(self, message, source, ):
        super().__init__(message)
        self.message = message
        self.source = source

    def __str__(self):
        return f'Error whilst trying to authenticate to {self.source}. Error: {self.message}'
