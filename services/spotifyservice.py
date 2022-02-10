import logging
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from data.song_utils import Song
from data.enums import Source
from data.song_utils import Playlist


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
        return self.__parseSpotifyResponseOfSearch(results)

    def getSongsInPlaylistById(self, playlistId, playlistName):
        results = self.authentication.playlist(playlistId)
        return self.__parseSpotifyResponseOfPlaylist(results, playlistName)

    # private parser for response of tracks
    def __parseSpotifyResponseOfSearch(self, results):
        songs = []
        for track in results['tracks']['items']:
            # yup, thats ugly but apperently thats the only way to parse spotipy resp into own objects
            currentSong = Song(track['name'], track['artists'][0]['name'], int(track['duration_ms']) / 1000,
                               Source.SPOTIFY, track['href'])
            songs.append(currentSong)
        return songs

    def __parseSpotifyResponseOfPlaylist(self, results, playlistName):
        playlist = Playlist(playlistName)
        for track in results['tracks']['items']:
            currentSong = Song(track['track']['name'], track['track']['artists'][0]['name'], int(track['track']['duration_ms']) / 1000,
                               Source.SPOTIFY, track['track']['href'])
            playlist.songs.append(currentSong)
        return playlist
