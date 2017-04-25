from typing import List, Set


def create_interval(a, b):
    return set(range(a, b+1))


def remove_duplicates_preserving_order(strings: List[str]) -> List[str]:
    found = set()
    result = list()

    for string in strings:
        if found.__contains__(string):
            continue
        found.add(string)
        result.append(string)

    return result


# remove_duplicates_not_preserving_order
def remove_duplicates_not_preserving_order(strings: List[str]) -> List[str]:
    return list(set(strings))


# count_unique
def count_unique(strings: List[str]) -> int:
    return len(set(strings))