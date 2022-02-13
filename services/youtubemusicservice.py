from ytmusicapi import YTMusic
import logging
import os




class YouTubeMusicService:
    def __init__(self):
        self.ytmusic = YTMusic('services/headers_auth.json')

    def searchWithKeyWord(self, keyword):
        return self.ytmusic.search(keyword)

    def getIdByName(self, song_name):
        song = self.ytmusic.search(song_name, limit=1)
        # TODO Filter search response for type, e.g. only songs, not artists
        if isinstance(song[0], dict):
            print(song[0]['videoId'])
            return song[0]['videoId']
        else:
            print(f'Not a Song{song}')
            return None

    def createPlaylist(self, playlist_name, playlist_description=None, privacy_status="PUBLIC"):
        playlist_id = self.ytmusic.create_playlist(playlist_name, playlist_description, privacy_status, None, None)
        # TODO Exception Handling
        #except PlaylistCreationError:
        #    logging.error(f'Error while creating YT-Music Playlist. Name: {playlist_name}')
        return playlist_id

    def addSongToPlaylist(self, playlistId, songId):
        self.ytmusic.add_playlist_items(playlistId, [songId])

    def createPlaylistFromLocalPlaylist(self, playlist):
        # create new playlist with name and get playlistId
        playlistId = self.createPlaylist(playlist.name)
        for song in playlist.songs:
            # for each song get YT-music id and add it to yt music playlist
            song.ytmusic_id = self.getIdByName(song.song_name)
            self.addSongToPlaylist(playlistId, song.ytmusic_id)
