#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from constants import *
from typing_extensions import Protocol
from typing import Dict
from datetime import datetime as dt
from results import AlbumResult, ArtistResult, TrackResult, iTunesResult
from artist import Artist
from album import Album
from utils import align_dict


class Track:
    """Represents an iTunes Track.
    """
    # The raw data from iTunes.
    raw: iTunesResult
    # The artist of the track.
    artist: Artist
    # The album of the track.
    album: Album
    # The track id.
    uid: int
    # The name of the track.
    name: str
    # The country where the album was released.
    country: str
    # The release date of the album.
    date: dt
    # The length of the track in seconds.
    time: float
    # The genre of the track.
    genre: str

    def __init__(self) -> None:
        self.type = 'Track'

    @staticmethod
    def from_result(result: TrackResult) -> 'Track':
        track: Track = Track()

        track.raw = result
        track.artist = Artist.from_track_result(result)
        track.album = Album.from_track_result(result)
        track.uid = result['trackId']
        track.name = result['trackCensoredName'] if CENSORED else result[
            'trackName']
        track.country = result['country']
        track.date = dt.strptime(result['releaseDate'], '%Y-%m-%dT%H:%M:%SZ')
        track.time = result['trackTimeMillis'] / 1000
        track.genre = result['primaryGenreName']

        return track

    def __str__(self) -> str:
        return self.name
