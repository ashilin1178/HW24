from functions import filter_query


def build_query(cmd: str, value: str, file_name: str):
    with open(file_name) as f:
        return list(filter_query(value, f))
