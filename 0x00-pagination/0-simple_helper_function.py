#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """the code Retrieves the index range from a given page and page size.
    """

    start_in = (page - 1) * page_size
    end_in = start_in + page_size
    return (start_in, end_in)
