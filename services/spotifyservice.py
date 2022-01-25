import logging
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv


class SpotifyService:
    def __init__(self):
        load_dotenv("variables.env")
        if os.getenv('CLIENT_ID') is None:
            logging.error("Envvars couldnt be loaded")
        self.authentication = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id=os.getenv('CLIENT_ID'),
                                                  client_secret=os.getenv('CLIENT_SECRET')))

    def getSongsByKeyword(self, keyword, limit, *args):
        songs = []
        """if args.limit is None:
            limit = 20"""
        results = self.authentication.search(q=keyword, limit=limit)
        #print(results)
        for idx, track in enumerate(results['tracks']['items']):
            song = (idx, track['name'])
            songs.append(song)
        return songs
