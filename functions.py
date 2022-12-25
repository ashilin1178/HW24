from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)

def unique_query(data, *args, **kwargs):
    return set(data)

def map_query(value: str, data: Iterable[str]):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)

def limit_query(value: str, data: Iterable[str]):
    limit = int(value)
    return list(data)[:limit]

def sort_query(value: str, data: Iterable[str]):
    reverse = value == 'desc'
    retu
