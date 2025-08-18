#!/usr/bin/env python3#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination.
This module contains a Server class for deletion-resilient pagination of a dataset.
"""

import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset

        Returns:
            List[List]: The cached dataset, omitting the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0

        Returns:
            Dict[int, List]: The dataset indexed by its original positions.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a deletion-resilient page from the indexed dataset.

        Args:
            index (int): The starting index for the page.
            page_size (int): The number of items per page.

        Returns:
            Dict: Dictionary with pagination info and page data.
        """
        assert index is not None and isinstance(index, int)
        indexed_dataset = self.indexed_dataset()
        assert index >= 0 and index < len(self.dataset())
        data = []
        current = index
        count = 0
        while count < page_size and current < len(self.dataset()):
            if current in indexed_dataset:
                data.append(indexed_dataset[current])
                count += 1
            current += 1
        next_index = current if current < len(self.dataset()) else None
        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
