=====
Usage
=====

To use Quran Tafseer Python Package in a project ::

    import pytafseer

List of Tafseer books
---------------------

To get a list of tafseer books available at the REST APIs ::

    from pytafseer import QuranTafseer

    books = QuranTafseer.get_tafseer_books()
    print(books)
    >>>
    [{'author': 'نخبة من العلماء',
      'book_name': 'التفسير الميسر',
      'id': 1,
      'language': 'ar',
      'name': 'التفسير الميسر'},
     {'author': 'جلال الدين المحلي و السيوطي',
      'book_name': 'تفسير الجلالين',
      'id': 2,
      'language': 'ar',
      'name': 'تفسير الجلالين'},
     {'author': 'عبد الرحمن بن ناصر بن عبد الله السعدي التميمي مفسر',
      'book_name': 'تيسير الكريم الرحمن في تفسير كلام المنان',
      'id': 3,
      'language': 'ar',
      'name': 'تفسير السعدي'},
     {'author': 'عماد الدين أبي الفداء إسماعيل بن كثير القرشي',
      'book_name': 'تفسير القرآن العظيم',
      'id': 4,
      'language': 'ar',
      'name': 'تفسير ابن كثير'},
     {'author': 'محمد سيد طنطاوي',
      'book_name': 'التفسير الوسيط للقرآن الكريم',
      'id': 5,
      'language': 'ar',
      'name': 'تفسير الوسيط لطنطاوي'},
     {'author': 'الحسين بن مسعود البغوي أبو محمد',
      'book_name': 'معالم التنزيل',
      'id': 6,
      'language': 'ar',
      'name': 'تفسير البغوي'},
     {'author': 'أبو عبد الله محمد بن أحمد الأنصاري القرطبي',
      'book_name': 'الجامع لأحكام القرآن',
      'id': 7,
      'language': 'ar',
      'name': 'تفسير القرطبي'},
     {'author': 'الإمام أبو جعفر الطبري',
      'book_name': 'جامع البيان في تأويل القرآن',
      'id': 8,
      'language': 'ar',
      'name': 'تفسير الطبري'},
     {'author': 'A. J. Arberry',
      'book_name': 'The Koran Interpreted',
      'id': 9,
      'language': 'en',
      'name': 'Arberry'},
     {'author': 'Abdullah Yusuf Ali',
      'book_name': 'The Meaning of the Glorious Koran',
      'id': 10,
      'language': 'en',
      'name': 'Yusuf Ali'},
     {'author': 'Salomo Keyzer',
      'book_name': 'De Koran, voorafgegaan door het leven van Mahomet',
      'id': 11,
      'language': 'nl',
      'name': 'Keyzer'},
     {'author': 'Fred Leemhuis',
      'book_name': 'De Koran: Een weergave van de betekenis van de Ara',
      'id': 12,
      'language': 'nl',
      'name': 'Leemhuis'},
     {'author': 'Sofian S. Siregar',
      'book_name': 'De Edele Koran, en een vertaling van betekenissen',
      'id': 13,
      'language': 'nl',
      'name': 'Siregar'}]

    
List of Tafseer books for one language
---------------------------------------

To get a list of tafseer books for one language available at the REST APIs ::

    from pytafseer import QuranTafseer

    books = QuranTafseer.get_tafseer_books(language='en')
    print(books)
    >>>
     [{'author': 'A. J. Arberry',
    'book_name': 'The Koran Interpreted',
    'id': 9,
    'language': 'en',
    'name': 'Arberry'},
    {'author': 'Abdullah Yusuf Ali',
    'book_name': 'The Meaning of the Glorious Koran',
    'id': 10,
    'language': 'en',
    'name': 'Yusuf Ali'}]

One verse Tafseer text
----------------------

To get tafseer for one verse in a chapter.

1. You should active one of the tafseer books.
2. Get the verse tafseer text from the book. ::
    
    tafseer = QuranTafseer(book_id=10)  # activate tafseer book
    verse_tafseer = tafseer.get_verse_tafseer(chapter_number=1,
                                             verse_number=1)
    print(verse_tafseer)
    >>>
    {'ayah_number': 1,
    'ayah_url': '/quran/1/1',
    'tafseer_id': 10,
    'tafseer_name': 'Yusuf Ali',
    'text': 'In the name of Allah, Most Gracious, Most Merciful.'}


Range of verses in a chapter Tafseer text
------------------------------------------

To get tafseer range of verses in a chapter.

1. You should active one of the tafseer books.
2. Get multiple verses tafseer text from the book. ::

    tafseer = QuranTafseer(book_id=10)  # activate tafseer book
    verses_tafseer = tafseer.get_verses_tafseer(chapter_number=1,
                                                    verse_number_from=1,
                                                    verse_number_to=2)
    print(verses_tafseer)
    >>>
    [{'ayah_number': 1,
    'ayah_url': '/quran/1/1',
    'tafseer_id': 10,
    'tafseer_name': 'Yusuf Ali',
    'text': 'In the name of Allah, Most Gracious, Most Merciful.'},
    {'ayah_number': 2,
    'ayah_url': '/quran/1/2',
    'tafseer_id': 10,
    'tafseer_name': 'Yusuf Ali',
    'text': 'Praise be to Allah, the Cherisher and Sustainer of the worlds;'}]



Verse Tafseer text with its Quran text
--------------------------------------

Sometimes you want to get the verse Quran text with its tafseer text.

1. You should active one of the tafseer books.
2. Get the verse tafseer from the book, but pass extra argument. ::
    
    tafseer = QuranTafseer(book_id=10)  # activate tafseer book
    verse_tafseer = tafseer.get_verse_tafseer(chapter_number=1,
                                              verse_number=1,
                                              with_verse_text=True)
    print(verse_tafseer['verse_text'])
    >>>
    {'ayah_number': 1,
    'ayah_url': '/quran/1/1',
    'tafseer_id': 10,
    'tafseer_name': 'Yusuf Ali',
    'text': 'In the name of Allah, Most Gracious, Most Merciful.',
    'verse_text': 'بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ'}


It's also working with getting the range.

1. You should active one of the tafseer books.
2. Get multiple verses tafseer from the book. ::

    tafseer = QuranTafseer(book_id=10)  # activate tafseer book
    verses_tafseer = tafseer.get_verses_tafseer(chapter_number=1,
                                                verse_number_from=1,
                                                verse_number_to=2,
                                                with_verse_text=True)
    print(verses_tafseer[0]['verse_text'])
    >>>بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
