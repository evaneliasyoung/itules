#!/usr/bin/env python3
"""
Author   : Evan Elias Young
Date     : 2020-03-14
Revision : 2020-03-14
"""

from constants import *
from typing import Tuple, List, Dict, Optional, Union
import sys
from utils import clear, pause
from utils import align_dict, print_centered
from album import Album
from artist import Artist
from track import Track
from wrapper import print_result, lookup_entity, search_entities


def print_header() -> None:
    """Prints the main header for iTules.
    """
    clear()
    print_centered('  _ _______    _           ')
    print_centered(' (_)__   __|  | |          ')
    print_centered('  _   | |_   _| | ___  ___ ')
    print_centered(' | |  | | | | | |/ _ \\/ __|')
    print_centered(' | |  | | |_| | |  __/\\__ \\')
    print_centered(' |_|  |_|\\__,_|_|\\___||___/')
    print_centered('                           ')
    print_centered(f'Version {VERSION}')
    print_centered(f'Copyright Evan Elias Young')
    print()


def get_menu_opt(menu_name: str,
                 options: Dict[str, str],
                 strict: bool = True) -> Tuple[str, List[str]]:
    """Displays a menu and returns a valid option.

    Arguments:
        menu_name {str} -- The menu's name.
        options {Dict[str, str]} -- The valid options and descriptions.

    Keyword Arguments:
        strict {bool} -- Whether or not to disallow options not in the dictionary. (default: {True})

    Returns:
        Tuple[str, List[str]] -- The chosen option, and any extra pieces.
    """
    # The user's selected option.
    opt: str = ''
    # The options and decsriptions.
    lines: List[str] = align_dict(options)
    # The max length of all the lines.
    max_line_len: int = max([len(k) for k in lines])
    # The number of spaces to put before the options.
    left_pad: int = round((LINE_LENGTH - max_line_len) / 2)

    while True:
        print_header()
        print_centered(f'{menu_name} MENU')
        for line in lines:
            print(f'{" ":{left_pad}}{line}')
        opt = input()
        if not (strict) or opt.split(' ')[0] in options:
            break
    return (opt.split(' ')[0], opt.split(' ')[1:])


def search_menu() -> None:
    """The search menu for iTules.
    """
    # Whether or not to keep the menu alive.
    keep_alive: bool = True

    while keep_alive:
        # The valid options the user can pick.
        choices: Dict[str, str] = {
            'song': 'search for a song',
            'album': 'search for a album',
            'artist': 'search for a artist',
            'all': 'search for any of the above',
            'back': 'go back',
            'exit': 'exit the program'
        }
        # The option the user has chosen.
        choice: str
        # Any extra input the user has entered.
        args: List[str]
        # Actually retrieve the data.
        choice, args = get_menu_opt('SEARCH', choices)

        if choice == 'exit':
            sys.exit(0)
        elif choice == 'back':
            keep_alive = False
        else:
            search_term: str = ' '.join(args)
            if len(args) == 0:
                print_header()
                print_centered(f'{choice.upper()} SEARCH MENU')
                search_term = input('enter your search term:\n')
            entity_name: str = 'song,album,musicArtist' if choice == 'all' else \
                'musicArtist' if choice == 'artist' else choice
            search_results: List[Union[Artist, Album,
                                       Track]] = search_entities(
                                           search_term, entity_name)
            clear()
            print_centered(f'{choice.upper()} SEARCH RESULTS')
            if len(search_results) > 0:
                for _, result in enumerate(search_results):
                    print_result(result)
            else:
                print_centered('NO RESULTS')
            pause()


def lookup_menu(uid: Optional[int]) -> None:
    """The lookup menu for iTules.
    """
    # Whether or not to keep the menu alive.
    keep_alive: bool = True

    while keep_alive:
        if not uid:
            # The valid options the user can pick.
            choices: Dict[str, str] = {
                'numeric': 'the ID to search for',
                'back': 'go back',
                'exit': 'exit the program'
            }
            # The option the user has chosen.
            choice: str
            # Actually retrieve the data.
            choice = get_menu_opt('LOOKUP', choices, False)[0]
        else:
            choice = str(uid)

        if choice == 'exit':
            sys.exit(0)
        elif choice == 'back':
            keep_alive = False
        elif choice.isdigit():
            keep_alive = False
            entity: Optional[Union[Artist, Album,
                                   Track]] = lookup_entity(int(choice))
            clear()
            print_centered('LOOKUP RESULTS')
            if entity:
                print_result(entity)
            else:
                print_centered('NO RESULTS')
            pause()


def main_menu() -> None:
    """The main menu for iTules.
    """
    # Whether or not to keep the menu alive.
    keep_alive: bool = True

    while keep_alive:
        # The valid options the user can pick.
        choices: Dict[str, str] = {
            'search': 'search the iTunes store by a term',
            'lookup': 'search the iTunes store by an entity ID',
            'exit': 'exit the program'
        }
        # The option the user has chosen.
        choice: str
        # Any extra input the user has entered.
        args: List[str]
        # Actually retrieve the data.
        choice, args = get_menu_opt('MAIN', choices)

        if choice == 'exit':
            sys.exit(0)
        elif choice == 'search':
            search_menu()
        elif choice == 'lookup':
            lookup_menu(int(args[0]) if len(args) > 0 else None)
