from ytmusicapi import YTMusic
import logging
import os

from data.enums import Source
from data.exceptions import AuthenticationException, PlaylistCreationException, SongException


class YouTubeMusicService:
    def __init__(self):
        self.ytmusic = YTMusic('services/headers_auth.json')

    def testAuthentication(self):
        # for startup, to test if authentication works
        try:
            self.ytmusic.search("test")
        except Exception:
            raise AuthenticationException("Error whilst Authenticating at Youtube Music", Source.YOUTUBE_MUSIC)

    def searchWithKeyWord(self, keyword):
        # search in YTM with a keyword
        return self.ytmusic.search(keyword)

    def getIdByName(self, song_name):
        searchResponse = self.ytmusic.search(song_name, limit=1)
        # getting the first song out of response, sometimes an artist or playlist gets returned as a first match
        # which needs to be filtered out
        for item in searchResponse:
            if item['resultType'] == "song":
                print(f'Song Name: {song_name}')
                return item['videoId']
        logging.log(f'no machting YouTube Song for {song_name} found')
        return None

    def createPlaylist(self, playlist_name, playlist_description, privacy_status="PUBLIC"):
        # Create a Playlist with name and a description, returns the new playlist id
        try:
            playlist_id = self.ytmusic.create_playlist(playlist_name, playlist_description, privacy_status)
            return playlist_id
        except:
            raise PlaylistCreationException("Failed to create Playlist", Source.YOUTUBE_MUSIC, playlist_name)

    def addSongToPlaylist(self, playlistId, songId):
        # add a Song to a specific Playlist
        try:
            self.ytmusic.add_playlist_items(playlistId, [songId])
        except:
            raise SongException(f"Failed to add Song to Playlist with id {playlistId}", Source.YOUTUBE_MUSIC, songId)

    def createPlaylistFromLocalPlaylist(self, playlist):
        # create new playlist with name and get playlistId
        playlistId = self.createPlaylist(playlist.name, playlist.playlist_description)
        for song in playlist.songs:
            # for each song get YT-music id and add it to yt music playlist
            song.ytmusic_id = self.getIdByName(song.song_name)
            self.addSongToPlaylist(playlistId, song.ytmusic_id)
