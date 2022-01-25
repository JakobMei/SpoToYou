import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyService:
    def __init__(self):
        self.authentication = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id="...",
                                                  client_secret="..."))

    def search(self, keyword):
        results = self.authentication.search(q=keyword, limit=20)
        print(results)
