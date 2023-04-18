from lecture_4 import get_queries_stats


QUERIES = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


def test_get_queries_stats():
    result = get_queries_stats(QUERIES)
    expected = ('Поисковые запросы с количеством слов "2" встречаются в 42.86% случаев.\n'
                'Поисковые запросы с количеством слов "3" встречаются в 57.14% случаев.')
    assert result == expected
