from ytmusicapi import YTMusic
import logging
import os

class YouTubeMusicService:
    def __init__(self):
        self.ytmusic = YTMusic('headers_auth.json')

    def searchWithKeyWord(self, keyword):
        return self.ytmusic.search(keyword)