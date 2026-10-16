"""Helpers that work on lists of test-case dicts (see generators.make_test_case)."""
from collections import Counter


def sort_cases(cases, field, reverse=False):
    """Return a NEW list sorted by `field` (e.g. 'duration'). The original list is not changed."""
    # TODO: sorted(cases, key=lambda case: case[field], reverse=reverse)
    return sorted(cases, key=lambda case: case[field], reverse = reverse)


def slowest(cases):
    """Return the case with the largest 'duration', or None if the list is empty."""
    # TODO: guard the empty list first; then max(..., key=lambda ...)
    if cases == []:
        return None
    else:
        return max(cases, key=lambda x: x["duration"])


def count_by(cases, field):
    """Return a plain dict counting cases per value of `field`: {'High': 2, 'Low': 1}."""
    # TODO: Counter over the field values, then dict(...) of it
    field_counts = Counter()
    for case in cases:
        field_counts[case[field]] += 1

    return field_counts