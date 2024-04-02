#!/usr/bin/env python3
"""This module aims at Implementing a method named get_page
that takes two integer arguments page with default value 1
and page_size with default value 10.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """takes two integer arguments page with default value 1 and
        page_size with default value 10.

        args:
            page - positional page or page to visit
            page_size - number of items to display per page.

        Returns: the appropriate page of the dataset (i.e.
        the correct list of rows)
        If the input arguments are out of range for the dataset,
        an empty list should be returned.
        """

        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        offset = (page * page_size) - page_size
        next_from = page * page_size
        data = self.dataset()
        return data[offset:next_from]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Implements a get_hyper method that takes the same arguments
        (and defaults) as get_page and returns a dictionary containing
        the following key-value pairs:

        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer
        """
        data = self.get_page(page, page_size)
        return {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': ((page + 1) if data else None),
            'prev_page': ((page - 1) if page > 0 else None),
            'total_pages': int(len(self.dataset()) / page_size)
        }
