#!/usr/bin/env python3

import os
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import warnings
import logging

import requests
from pyquery import PyQuery as pq

SEARCH_ENDPOINT = 'https://webcat.hkpl.gov.hk/search/syndication?match_1=PHRASE&field_1=isbn&term_1={0}&sort=relevance&syndication=true'
LIBRARY_LOCATION = os.getenv('LIBRARY_LOCATION', '904200000')
HEADERS = {
    'Accept-Language': 'en-US,en;q=0.8'
}
logger = logging.getLogger('hkpl-searcher')
logging.basicConfig(format='[%(name)s / %(levelname)s] %(message)s', level=logging.INFO)
lock = Lock()


def search_book(isbn: str):
    logger.debug('Searching for book. ISBN: %s', isbn)
    res = requests.get(SEARCH_ENDPOINT.format(isbn), headers=HEADERS)
    res.raise_for_status()

    q = pq(res.content)
    if not q('item'):
        logger.debug('Book does not exists. ISBN: %s', isbn)
        return

    detail_url = q('item > guid').text()
    return book_detail(isbn, detail_url)


def book_detail(isbn: str, url: str):
    res = requests.get(url.replace('system', 'WEB') + '&loc=' + LIBRARY_LOCATION, headers=HEADERS)
    res.raise_for_status()

    q = pq(res.content)

    # Check if isbn matches
    # Library search suggestion may troll
    retrived_isbn = q('#itemView tr:nth-child(10) span').text()
    if retrived_isbn != isbn:
        logger.debug('Book is not available in library. Search suggestion of library has trolled')
        return

    # Check if book is available
    if not q('table.table'):
        logger.debug('Book is not available in targeted library')
        return

    for _el in q('table.table tr.odd, table.table tr.even'):
        el = pq(_el)
        status = el.children('td:nth-child(5)').text().strip()
        logger.debug('status: %s', status)
        if status == 'Available' or status == '館內架上':
            break
    else:
        # Not found
        logger.debug('Book is not on shelf in targeted library')
        return

    # Book is available now. Get book information
    return get_book_info(res)


def get_book_info(res: requests.Request):
    q = pq(res.content)

    return {
        'title': q('.title').text(),
        'detail_url': res.url
    }


def execute(isbn: str, index: int):
    information = search_book(isbn)

    if information is None:
        return

    with lock:
        print(index+1, information['title'], information['detail_url'])


def main():
    warnings.filterwarnings('ignore')
    executor = ThreadPoolExecutor(max_workers=10)
    with open('books') as file:
        isbns = file.read().split('\n')
    for i, isbn in enumerate(isbns):
        executor.submit(execute, isbn, i)


if __name__ == '__main__':
    main()
