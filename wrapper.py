#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from constants import *
from typing import Optional, Union, List, Dict, Any
import requests
import json
from results import AlbumResult, ArtistResult, TrackResult, iTunesResponse, iTunesResult
from album import Album
from artist import Artist
from track import Track


def lookup(
        uid: int) -> Optional[iTunesResult]:
    """Sends a lookup request with a given id.

    Arguments:
        uid {int} -- The entity id.

    Returns:
        Optional[iTunesResult] -- The raw data returned by iTunes.
    """
    data: Optional[iTunesResult] = None
    try:
        response: requests.Response = requests.get(
            'https://itunes.apple.com/lookup', params={'id': uid})
        data = json.loads(response.content.decode('utf-8'))['results'][0]
    except:
        data = None
    return data


def lookup_entity(uid: int) -> Optional[Union[Artist, Album, Track]]:
    # Get the raw data.
    data: Optional[iTunesResult] = lookup(uid)
    entity: Optional[Union[Artist, Album, Track]] = None
    if data:
        entity = derive_entity(data).from_result(data)
    return entity


def search(term: str, entity: str) -> iTunesResponse:
    """Sends a search request with a given term and entity type.

    Arguments:
        term {str} -- The search term.
        entity {str} -- The entity type(s).

    Returns:
        iTunesResponse -- The raw data returned by iTunes.
    """
    # The starting index of the actual data.
    start: int = 13
    # The ending index of the actual data.
    stop: int = -5
    # The search parameters.
    params: Dict[str, str] = {
        'output': 'json',
        'callback': 'JSONP.run',
        'term': term,
        'country': SEARCH_COUNTRY,
        'media': SEARCH_MEDIA,
        'entity': entity,
        'limit': str(SEARCH_LIMIT),
        'lang': SEARCH_LANG
    }
    # The response for the request.
    response: requests.Response = requests.get(
        'https://itunes.apple.com/search', params=params)
    # The json data.
    data: iTunesResponse = json.loads(
        response.content.decode('utf-8')[start:stop])
    return data


def search_entities(term: str,
                    entity: str) -> List[Union[Artist, Album, Track]]:
    """Sends a search request with a given term and entity type.

    Arguments:
        term {str} -- The search term.
        entity {str} -- The entity type(s).

    Returns:
        List[Union[Artist, Album, Track]] -- A list of entities returned by iTunes.
    """
    # Get the raw data.
    data: iTunesResponse = search(term, entity)
    # Create the list of results.
    results: List[Union[Artist, Album, Track]] = []
    # The current entity when iterating.
    cur_ent: Union[Artist, Album, Track]

    for raw_ent in data['results']:
        cur_ent = derive_entity(raw_ent).from_result(raw_ent)
        results.append(cur_ent)
    return results


def derive_entity(
    data: iTunesResult
) -> Union[Artist, Album, Track]:
    """Derives the entity type given raw data from iTunes.

    Arguments:
        data {iTunesResult} -- The raw data returned by iTunes.

    Raises:
        NotImplementedError: An uncoded wrapper type was returned.

    Returns:
        Union[Artist, Album, Track] -- The entity
    """
    entity: Union[Artist, Album, Track]
    if data['wrapperType'] == 'collection':
        entity = Album()
    elif data['wrapperType'] == 'track':
        entity = Track()
    elif data['wrapperType'] == 'artist':
        entity = Artist()
    else:
        raise NotImplementedError(
            f'"{data["wrapperType"]}" not a known wrapper type')
    return entity


def print_result(coll: Union[Artist, Album, Track]) -> None:
    """Prints the search results.

    Arguments:
        coll {Union[Artist, Album, Track]} -- The entity.
    """
    print(f'{coll.uid:<{MAX_ID_LEN}}', end=SPACES)
    if len(coll.name) > MAX_NAME_LEN:
        # entity name too big, trim it.
        print(f'{coll.name[:MAX_NAME_LEN]:{MAX_NAME_LEN}}', end='...   ')
    else:
        print(f'{coll.name:{MAX_NAME_LEN}}', end=SPACES * 2)
    if not isinstance(coll, Artist):
        # not an artist, so it has an artist field.
        if len(coll.artist.name) > MAX_ARTIST_LEN:
            # artist name too big, trim it.
            print(f'{coll.artist.name[:MAX_ARTIST_LEN]:{MAX_ARTIST_LEN}}',
                  end='...')
        else:
            print(f'{coll.artist.name:{MAX_ARTIST_LEN}}', end=SPACES * 2)
    print()
