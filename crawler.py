"""
A simple-to-use web worker that collects
website data as it crawls

Author: Mark Boon
Date: 25/08/2017
Version: 2.2.1
"""

import threading
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class Worker:
    base_url = ''
    queue = []
    lock = threading.Semaphore(value=1)

    def __init__(self, base_url):
        self.base_url = base_url
        self.queue = [base_url]

    @staticmethod
    def write_file(path, data):
        with open(path, 'a') as f:
            f.write(data)
            f.close()

    def report(self, url):
        self.lock.acquire()
        print("Successfully crawled", url)
        self.lock.release()

    def work(self):
        for link in self.queue:

            try:
                page = urlopen(link)
                soup = BeautifulSoup(page, 'lxml')

                self.write_file("dump.txt", soup.text)
                self.write_file("log.txt", link + "\n")
                self.report(link)

                for upper in soup.find_all('a', href=True):
                    dom = urljoin(self.base_url, upper['href'])
                    if dom not in set(self.queue):
                        self.queue.append(dom)

            except:
                self.write_file("error_log.txt", str(link) + "\n")
                pass
