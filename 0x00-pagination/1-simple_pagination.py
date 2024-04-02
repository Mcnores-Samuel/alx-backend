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
