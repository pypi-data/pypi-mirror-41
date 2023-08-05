# -*- coding: utf-8 -*-

"""Top-level package for PyTafseer Python Package."""
from urllib.parse import urljoin

import requests

from .settings import WEB_API_URL

__author__ = """Emad Mokhtar"""
__email__ = 'emad.m.habib@gmail.com'
__version__ = '0.1'


class QuranTafseer:
    @classmethod
    def get_tafseer_books(cls, language='') -> list:
        """Gets the list of available tafseer

        :param language: filter the list of tafseer based on language,
            defaults, `ISO 639-1 language
            <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ optional.


        :raises ValueError: raise Value error if the JSON return form the
                services is invalid.  #noqa
        :raises Timeout: if the server didn't return any response.
        :raises HTTPError: if the server returned unsuccessful response.


        :return: list of dictionary with tafseer attributes ['id', 'name',
                 'language', 'author', 'book_name']
        """

        params = {}
        if language:
            params['lang'] = language
        request_url = urljoin(WEB_API_URL, 'tafseer')
        response = requests.get(request_url, params=params)
        response.raise_for_status()
        return response.json()

    def __init__(self, book_id: int) -> None:
        self.book_id = book_id
        self.base_url = '{}/tafseer/{}'.format(WEB_API_URL,
                                               book_id)

    def get_verse_tafseer(self, chapter_number: int, verse_number: int,
                          with_verse_text: bool = False) -> dict:
        """Gets the tafseer text for one verse

        :param with_verse_text: Whether to load the verse Quran text or not.
        :param chapter_number: Chapter number.
        :param verse_number: Verse number or a start range.
        """
        request_url = '{}/{}/{}'.format(self.base_url,
                                        chapter_number,
                                        verse_number)
        response = requests.get(request_url)
        response.raise_for_status()
        tafseer_dict = response.json()
        if with_verse_text:
            verse_text_url = urljoin(WEB_API_URL, tafseer_dict['ayah_url'])
            tafseer_dict['verse_text'] = self._get_verse_text(verse_text_url)
        return tafseer_dict

    def get_verses_tafseer(self, chapter_number: int,
                           verse_number_from: int,
                           verse_number_to: int,
                           with_verse_text: bool = False) -> list:
        """Gets the tafseer text for a range of verses

        :param with_verse_text: Whether to load the verse Quran text or not.
        :param chapter_number: Chapter number.
        :param verse_number_from: Verse number start range.
        :param verse_number_to: Verse number end range.
        """
        request_url = '{}/{}/{}/{}'.format(
            self.base_url,
            chapter_number,
            verse_number_from,
            verse_number_to)
        response = requests.get(request_url)
        response.raise_for_status()
        tafseer_dict = response.json()
        if with_verse_text:
            for verse in tafseer_dict:
                verse_text_url = urljoin(WEB_API_URL, verse['ayah_url'])
                verse['verse_text'] = self._get_verse_text(verse_text_url)
        return tafseer_dict

    def _get_verse_text(self, url: str) -> str:
        """Gets verse Quran text.

        :param url: URL to make a request to get the verse text
        :return: The verse text
        """

        verse_text_url = urljoin(WEB_API_URL, url)
        verse_text_res = requests.get(verse_text_url)
        verse_text_res.raise_for_status()
        return verse_text_res.json()['text']
