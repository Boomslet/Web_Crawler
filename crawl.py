"""
Web crawler (WIP)

Author: Mark Boon
Date: 24/07/2017
Version: -
"""

import os
import urllib.request
from bs4 import BeautifulSoup, SoupStrainer

url_list = []


def create_dirs(url_name):
    if not os.path.exists(url_name):
        print('Creating ' + url_name)
        os.makedirs(url_name)


def write_file(path, data):
    with open(path, 'a') as f:
        f.write(data)


def crawler(base_url, element="tr", keyword=None):
    
    url_list.append(base_url)

    for url in url_list:
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, "html.parser")
        data = soup.find_all(element)

        for link in BeautifulSoup(page, parseOnlyThese=SoupStrainer('a')):
            if link.has_attr('href'):
                url_list.append(link['href'])

