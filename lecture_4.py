def get_geo_logs_by_country(country, geo_logs):
    return list(filter(lambda visit: list(*visit.values())[1] == country, geo_logs))


def get_unique_ids(ids):
    unique_ids = {}
    for geo_ids in ids.values():
        for geo_id in geo_ids:
            unique_ids[geo_id] = None
    return list(unique_ids.keys())


def get_queries_stats(queries):
    queries_stats = {}
    for query in queries:
        queries_stats.setdefault(len(query.split()), 0)
        queries_stats[len(query.split())] += 1
    queries_stats = dict(sorted(queries_stats.items()))
    total_queries_amount = sum(queries_stats.values())
    result = []
    for words_amount, queries_amount in queries_stats.items():
        percent = queries_amount / total_queries_amount * 100
        result.append(f'Поисковые запросы с количеством слов "{words_amount}" встречаются в {percent:.2f}% случаев.')
    return '\n'.join(result)
