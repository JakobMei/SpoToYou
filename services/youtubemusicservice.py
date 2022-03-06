from ytmusicapi import YTMusic
import logging
import os




class YouTubeMusicService:
    def __init__(self):
        self.ytmusic = YTMusic('services/headers_auth.json')

    def searchWithKeyWord(self, keyword):
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
        playlist_id = self.ytmusic.create_playlist(playlist_name, playlist_description, privacy_status)
        # TODO Exception Handling
        #except PlaylistCreationError:
        #    logging.error(f'Error while creating YT-Music Playlist. Name: {playlist_name}')
        return playlist_id

    def addSongToPlaylist(self, playlistId, songId):
        self.ytmusic.add_playlist_items(playlistId, [songId])

    def createPlaylistFromLocalPlaylist(self, playlist):
        # create new playlist with name and get playlistId
        playlistId = self.createPlaylist(playlist.name, playlist.playlist_description)
        for song in playlist.songs:
            # for each song get YT-music id and add it to yt music playlist
            song.ytmusic_id = self.getIdByName(song.song_name)
            self.addSongToPlaylist(playlistId, song.ytmusic_id)
