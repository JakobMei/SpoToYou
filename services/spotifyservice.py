import logging
import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from data.song_utils import Song
from data.enums import Source
from data.song_utils import Playlist
from data.exceptions import AuthenticationException, PlaylistException


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

    def testAuthentication(self):
        # for startup, to test if authentication worked
        try:
            self.authentication.search("test")
        except Exception:
            raise AuthenticationException("Error whilst authenticating at Spotity", Source.SPOTIFY)

    def getSongsByKeyword(self, keyword, limit=20):
        # to get one or more songs from a specific keyword

        # response is structured as follows: results{tracks{items[name, album{} duration in ms, href, popularity,
        # uri, artists[id, name, href, id]]}}
        results = self.authentication.search(q=keyword, limit=limit)
        # print(results)
        return self._parseSpotifyResponseOfSearch(results)

    def getSongsInPlaylistById(self, spotify_playlistId, playlistName=None, playlistDescription=None):
        # to get all songs in a given playlist
        try:
            results = self.authentication.playlist(spotify_playlistId)
        except Exception:
            raise PlaylistException(Source.SPOTIFY)
        if playlistName is None:
            playlistName = results['name']
        if playlistDescription is None:
            playlistDescription = ""
        playlist = Playlist(playlistName, spotify_playlistId, None, playlistDescription)
        return self._parseSpotifyResponseOfPlaylist(results, playlist)

    # private parser for response of tracks
    def _parseSpotifyResponseOfSearch(self, results):
        songs = []
        for track in results['tracks']['items']:
            # yup, that's ugly but apparently that's the only way to parse spotipy resp into own objects
            currentSong = Song(track['name'], track['artists'][0]['name'], int(track['duration_ms']) / 1000,
                               Source.SPOTIFY, track['id'], None)
            songs.append(currentSong)
        return songs

    def _parseSpotifyResponseOfPlaylist(self, results, playlist):
        for track in results['tracks']['items']:
            # structure of playlist response from spotify is slightly different to normal search resp,
            # so an individual parser is necessary
            currentSong = Song(track['track']['name'], track['track']['artists'][0]['name'],
                               int(track['track']['duration_ms']) / 1000, Source.SPOTIFY, track['track']['id'], None)
            playlist.songs.append(currentSong)
        return playlist
