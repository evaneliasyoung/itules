#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from constants import *
from typing import Dict, List, Any
import os


def align_dict(collection: Dict[Any, Any]) -> List[str]:
    """Aligns items in a dictionary by key.

    Arguments:
        collection {Dict[Any, Any]} -- The dictionary to align.

    Returns:
        List[str] -- A list of lines aligned by key.
    """
    # The max length of all the keys.
    max_key_len: int = max([len(k) for k in collection])
    # The keys and descriptions.
    lines: List[str] = [
        f'{key:{max_key_len}} -- {collection[key]}'
        for _, key in enumerate(collection)
    ]
    return lines


def print_centered(text: str, width: int = LINE_LENGTH) -> None:
    """Prints text centered in the menus.

    Arguments:
        text {str} -- The text to print.

    Keyword Arguments:
        width {int} -- The width of the container (default: {LINE_LENGTH})
    """
    print(f'{text:^{width}}')


def clear() -> None:
    """Clears the screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def pause() -> None:
    """Prompts the user to press any key to continue.
    """
    os.system('pause' if os.name == 'nt' else
              'read -n1 -r -p "Press any key to continue . . . " key')
