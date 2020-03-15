#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from typing import List, Union, TypedDict


class AlbumResult(TypedDict):
    """Represents a result of type Artist from iTunes.
    """
    wrapperType: str
    collectionType: str
    artistId: int
    collectionId: int
    amgArtistId: int
    artistName: str
    collectionName: str
    collectionCensoredName: str
    artistViewUrl: str
    collectionViewUrl: str
    artworkUrl60: str
    artworkUrl100: str
    collectionPrice: float
    collectionExplicitness: str
    trackCount: int
    copyright: str
    country: str
    currency: str
    releaseDate: str
    primaryGenreName: str


class ArtistResult(TypedDict):
    """Represents a result of type Artist from iTunes.
    """
    wrapperType: str
    artistType: str
    artistName: str
    artistLinkUrl: str
    artistId: int
    amgArtistId: int
    primaryGenreName: str
    primaryGenreId: int


class TrackResult(TypedDict):
    """Represents a result of type Track from iTunes.
    """
    wrapperType: str
    kind: str
    artistId: int
    collectionId: int
    trackId: int
    artistName: str
    collectionName: str
    trackName: str
    collectionCensoredName: str
    trackCensoredName: str
    artistViewUrl: str
    collectionViewUrl: str
    trackViewUrl: str
    previewUrl: str
    artworkUrl30: str
    artworkUrl60: str
    artworkUrl100: str
    collectionPrice: int
    trackPrice: int
    releaseDate: str
    collectionExplicitness: str
    trackExplicitness: str
    discCount: int
    discNumber: int
    trackCount: int
    trackNumber: int
    trackTimeMillis: int
    country: str
    currency: str
    primaryGenreName: str
    isStreamable: bool


iTunesResult = Union[AlbumResult, ArtistResult, TrackResult]


class iTunesResponse(TypedDict):
    """Represents a response from iTunes.
    """
    resultCount: int
    results: List[Union[AlbumResult, ArtistResult, TrackResult]]
