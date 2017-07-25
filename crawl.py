"""
Web crawler (WIP)
Author: Mark Boon
Date: 24/07/2017
Version: -
"""

import lxml
import os
import requests
from bs4 import BeautifulSoup, SoupStrainer

url_list = []
crawled_list = []


def create_dirs(url_name):
    ind = url_name.find(".") + 1
    url_name = url_name[ind:]
    if not os.path.exists(url_name):
        print('Creating ' + url_name)
        os.makedirs(url_name)


def write_file(path, data):
    with open(path, 'a') as f:
        f.write(data)


def crawler(base_url, element="body", keyword=None):
    
    url_list.append(base_url)

    for url in url_list:
        
        crawled_list.append(url)
        url_list.remove(url)

        create_dirs(url)
        
        page = requests.get(url).text
        soup = BeautifulSoup(page, 'lxml')
        data = soup.find_all(element)
        write_file("dump.txt", soup.text)

        for link in BeautifulSoup(page, 'lxml', parse_only=SoupStrainer('a', href=True)):
            for link in soup.find_all('a'):
                try:
                    uDom = link['href']
                    url_list.append(url + uDom)
                except:
                    pass
