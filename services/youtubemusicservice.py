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
        return song
