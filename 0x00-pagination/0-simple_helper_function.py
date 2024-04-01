#!/usr/bin/env python3
"""This module has an index_range function for returning a
tuple of size two containing a start index and an end index
corresponding to the range of indexes to return in a list for
those particular pagination parameters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """Returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters.
    """
    return ((page * page_size) - page_size), (page * page_size)
