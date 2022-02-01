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
        # authenticate with ID and secret to Spotify, necessary so that spotify answers the requests. otherwise
        # they'd return a 4xxhttp  error
        self.authentication = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(client_id=os.getenv('CLIENT_ID'),
                                                  client_secret=os.getenv('CLIENT_SECRET')))

    def getSongsByKeyword(self, keyword, limit=20, *args):
        # response is structured as follows: results{tracks{items[namme, album{} duration in ms, href, popularity,
        # uri, artists[id, name, href, id]]}}
        results = self.authentication.search(q=keyword, limit=limit)
        # print(results)
        return self.parseSpotifyResponseOfSearch(results)

    def getSongsInPlaylistById(self, playlistId):
        results = self.authentication.playlist(playlistId)
        return self.parseSpotifyResponseOfPlaylist(results)

    # private parser for response of tracks
    def parseSpotifyResponseOfSearch(self, results):
        songs = []
        for idx, track in enumerate(results['tracks']['items']):
            song = (idx, track['name'], track['href'], track['artists'][0]['name'], track['duration_ms'])
            songs.append(song)
        return songs

    def parseSpotifyResponseOfPlaylist(self, results):
        songs = []
        for idx, track in enumerate(results['tracks']['items']['track']):
            song = (idx, track['name'], track['href'], track['artists'][0]['name'], track['duration_ms'])
            songs.append(song)
        return songs