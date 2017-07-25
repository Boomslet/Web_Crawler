"""
Web crawler (WIP)
Author: Mark Boon
Date: 24/07/2017
Version: -
"""

import lxml
import requests
from bs4 import BeautifulSoup, SoupStrainer
import util


url_list = []
crawled_list = []


def crawler(base_url, element="body"):
    url_list.append(base_url)

    for url in url_list:     
        crawled_list.append(url)
        url_list.remove(url)
        
        try:
            util.create_dirs(url)
            page = requests.get(url).text
            soup = BeautifulSoup(page, 'lxml')
            data = soup.find_all(element)
            util.write_file("dump.txt", soup.text)

            for link in BeautifulSoup(page, 'lxml', parse_only=SoupStrainer('a', href=True)):
                for link in soup.find_all('a'):
                    uDom = link['href']
                    url_list.append(uDom)
        except:
            
            pass

