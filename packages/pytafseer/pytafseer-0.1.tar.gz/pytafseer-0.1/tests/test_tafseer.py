from pytafseer import QuranTafseer
import pytest


@pytest.mark.vcr()
def test_get_tafseer_books():
    tafseer_list = QuranTafseer.get_tafseer_books()
    assert tafseer_list is not None
    assert list(tafseer_list[0].keys()).sort() == ['id', 'name', 'language', 'author',
                                                   'book_name'].sort()


@pytest.mark.vcr()
def test_get_tafseer_books_with_lang():
    tafseer_list = QuranTafseer.get_tafseer_books()
    tafseer_list_with_lang = QuranTafseer.get_tafseer_books(language='ar')
    assert len(tafseer_list) > len(tafseer_list_with_lang)


@pytest.mark.vcr()
def test_get_tafseer_text_one_verse():
    book = QuranTafseer(1)
    tafseer_text = book.get_verse_tafseer(1, 1)
    assert list(tafseer_text.keys()).sort() == ['tafseer_id', 'tafseer_name',
                                                'ayah_url', 'ayah_number',
                                                'text'].sort()


@pytest.mark.vcr()
def test_get_tafseer_text_one_verse_with_its_text():
    book = QuranTafseer(1)
    tafseer_text = book.get_verse_tafseer(1, 1, with_verse_text=True)
    assert list(tafseer_text.keys()).sort() == ['tafseer_id', 'tafseer_name',
                                                'ayah_url', 'ayah_number',
                                                'text', 'verse_text'].sort()


@pytest.mark.vcr()
def test_get_tafseer_text_range_verse():
    book = QuranTafseer(1)
    tafseer_text = book.get_verses_tafseer(1, 1, 2)
    assert len(tafseer_text) == 2


@pytest.mark.vcr()
def test_get_tafseer_text_range_verse_with_text():
    book = QuranTafseer(1)
    tafseer_text = book.get_verses_tafseer(1, 1, 2, with_verse_text=True)
    assert list(tafseer_text[0].keys()).sort() == ['tafseer_id', 'tafseer_name',
                                                   'ayah_url', 'ayah_number',
                                                   'text', 'verse_text'].sort()
