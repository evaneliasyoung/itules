#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from constants import *
from typing import Optional
from typing_extensions import Protocol
from datetime import datetime as dt
from results import AlbumResult, ArtistResult, TrackResult, iTunesResult
from artist import Artist


class Album:
    """Represents an iTunes Album.
    """
    # The raw data from iTunes.
    raw: iTunesResult
    # The artist of the album.
    artist: Artist
    # The album id.
    uid: int
    # The name of the album.
    name: str
    # The number of tracks in the album.
    trackCount: int
    # The copyright information of the album.
    copyright: str
    # The country where the album was released.
    country: str
    # The release date of the album.
    date: dt
    # The genre of the album.
    genre: str

    def __init__(self) -> None:
        self.type = 'Album'

    @staticmethod
    def from_result(result: AlbumResult) -> 'Album':
        album: Album = Album()

        album.raw = result
        album.artist = Artist.from_album_result(result)
        album.uid = result['collectionId']
        album.name = result['collectionCensoredName'] if CENSORED else result[
            'collectionName']
        album.trackCount = result['trackCount']
        album.copyright = result['copyright']
        album.country = result['country']
        album.date = dt.strptime(result['releaseDate'], '%Y-%m-%dT%H:%M:%SZ')
        album.genre = result['primaryGenreName']

        return album

    @staticmethod
    def from_track_result(result: TrackResult) -> 'Album':
        album: Album = Album()

        album.raw = result
        album.artist = Artist.from_track_result(result)
        album.uid = result['collectionId']
        album.name = result['collectionCensoredName'] if CENSORED else result[
            'collectionName']
        album.trackCount = result['trackCount']
        album.country = result['country']
        album.date = dt.strptime(result['releaseDate'], '%Y-%m-%dT%H:%M:%SZ')
        album.genre = result['primaryGenreName']

        return album

    def __str__(self) -> str:
        return self.name
