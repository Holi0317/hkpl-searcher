#!/usr/bin/env python3

import warnings
import logging
from urllib.parse import urlparse, parse_qs

import requests
from pyquery import PyQuery as pq

ENTRY = 'https://webcat.hkpl.gov.hk/search/query?theme=WEB'
logger = logging.getLogger('hkpl-searcher')
logging.basicConfig(format='[%(name)s / %(levelname)s] %(message)s', level=logging.INFO)


def get_library_list():
    res = requests.get(ENTRY)
    res.raise_for_status()

    q = pq(res.content)

    libraries = q('ul#id28 a:not(.showMore)')

    return [process_library(library) for library in libraries]


def process_library(q_: pq):
    q = pq(q_)
    link = q.attr('href')
    name = q.text().strip()

    p_url = urlparse(link)
    qs = parse_qs(p_url.query)
    id_ = qs['facet_loc'][0]

    return {
        'name': name,
        'id': id_
    }


def main():
    warnings.filterwarnings('ignore')
    libraries = get_library_list()
    for library in libraries:
        print(f"{library['name']} - {library['id']}")


if __name__ == "__main__":
    main()
