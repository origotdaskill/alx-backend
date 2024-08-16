#!/usr/bin/env python3

import csv
import math
from typing import Dict, List

index_range = __import__('0-simple_helper_function').index_range


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
        """
        Takes 2 args and returns the requested page number
        page: the requested page number
        page_size: number of records per page
        both params must be int and > 0
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        try:
            idx = index_range(page, page_size)
            return data[idx[0]:idx[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
            page_size: the length of the returned data set page
            page: the current page number
            data: the dataset page
            next_page: number of the next page, None if no page
            prev_page: number of the previous page, None if no page
            total_pages: total number of pages in the data set
            return a dict of the above info
        """
        total_pages = (len(self.dataset()) // page_size) + 1

        data = self.get_page(page, page_size)

        dict_t = {
            'page_size': page_size if page_size <= len(data) else len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 <= total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
        return dict_t
