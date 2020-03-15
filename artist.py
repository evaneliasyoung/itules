#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from constants import *
from typing_extensions import Protocol
from results import AlbumResult, ArtistResult, TrackResult, iTunesResult


class Artist:
    """Represents an iTunes Artist.
    """
    # The raw data from iTunes.
    raw: iTunesResult
    # The artist id.
    uid: int
    # The name of the artist.
    name: str
    # The genre of the artist.
    genre: str

    def __init__(self) -> None:
        self.type = 'Artist'

    @staticmethod
    def from_result(result: ArtistResult) -> 'Artist':
        artist: Artist = Artist()

        artist.raw = result
        artist.uid = result['artistId']
        artist.name = result['artistName']
        artist.genre = result['primaryGenreName']

        return artist

    @staticmethod
    def from_album_result(result: AlbumResult) -> 'Artist':
        artist: Artist = Artist()

        artist.raw = result
        artist.uid = result['artistId']
        artist.name = result['artistName']
        artist.genre = result['primaryGenreName']

        return artist

    @staticmethod
    def from_track_result(result: TrackResult) -> 'Artist':
        artist: Artist = Artist()

        artist.raw = result
        artist.uid = result['artistId']
        artist.name = result['artistName']
        artist.genre = result['primaryGenreName']

        return artist

    def __str__(self) -> str:
        return self.name
