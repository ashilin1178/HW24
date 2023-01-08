import re
from typing import Iterable, List, Set


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda x: value in x, data)


def unique_query(data: Iterable[str], *args, **kwargs) -> Set[str]:
    return set(data)


def map_query(value: str, data: Iterable[str]):
    col_number = int(value)
    return map(lambda x: x.split(' ')[col_number], data)


def limit_query(value: str, data: Iterable[str]) -> List[str]:
    limit = int(value)
    return list(data)[:limit]


def sort_query(value: str, data: Iterable[str]) -> List[str]:
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)


def regex_query(value: str, data: Iterable[str]) -> List[str]:
    for line in data:
        query_ = re.search(value, line)
        if query_:
            yield line
