#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

AUTHOR: str = 'Evan Elias Young'
DATE: str = '2020-03-14'
REVISION: str = '2020-03-14'
VERSION: str = '0.2.0'
DESCRIPTION: str = 'Search tools for the iTunes store.'
COPYRIGHT: str = 'Copyright Evan Elias Young 2020'

# The max length for the id printer.
MAX_ID_LEN: int = 11
# The max length for the album printer.
MAX_NAME_LEN: int = 32
# The max length for the artist printer.
MAX_ARTIST_LEN: int = 17
# The number of spaces inbetween standard fields.
SPACES_NUM: int = 3
# The spaces inbetween standard fields.
SPACES: str = ' ' * SPACES_NUM
# The dots sand spaces between cut fields.
DOTS: str = f'{"." * SPACES_NUM}{SPACES}'
# The number of characters in each line.
LINE_LENGTH: int = 4 + MAX_ID_LEN + MAX_NAME_LEN + MAX_ARTIST_LEN + SPACES_NUM * 5
assert LINE_LENGTH <= 79, f'line length too large, {LINE_LENGTH}'
# The default for the country option.
SEARCH_COUNTRY: str = 'US'
# The default for the media option.
SEARCH_MEDIA: str = 'music'
# The default for the entity option.
SEARCH_LIMIT: int = 10
# The default for the lang option.
SEARCH_LANG: str = 'en_us'
# Whether or not the program is censored.
CENSORED: bool = False
