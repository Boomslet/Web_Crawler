"""
Author: Mark Boon
Date: 30/07/2017
Version: 1.3.1
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request


class Crawler:
    base_url = ''
    queue = []

    def __init__(self, base_url):
        Crawler.base_url = base_url
        Crawler.queue = [base_url]

    @staticmethod
    def write_file(path, data):
        with open(path, 'a') as f:
            f.write(data)
            f.close()

    def work(self):
        for link in self.queue:

            try:
                page = urllib.request.urlopen(link)
                soup = BeautifulSoup(page, 'lxml')

                self.write_file("dump.txt", soup.text.strip("\n"))
                self.write_file("log.txt", link + "\n")

                print("Successfully crawled", link)

                for link in soup.find_all('a'):
                    dom = urljoin(self.base_url, link['href'])
                    if dom not in set(Crawler.queue):
                        self.queue.append(dom)

            except:
                pass