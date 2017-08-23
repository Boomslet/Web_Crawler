"""
A simple-to-use web worker that collects
website data as it crawls

Makes use of:
BeautifulSoup (pip install bs4),
lxml          (pip install lxml),

Author: Mark Boon
Date: 23/08/2017
Version: 2.1.1
"""

from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib.request
import threading


class worker:
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
                page = urllib.request.urlopen(link)
                soup = BeautifulSoup(page, 'lxml')

                self.write_file("dump.txt", soup.text)
                self.write_file("log.txt", link + "\n")
                self.report(link)
                
                for link in soup.find_all('a', href=True):
                    dom = urljoin(self.base_url, link['href'])
                    if dom not in set(self.queue):
                        self.queue.append(dom)

            except:
                self.write_file("error_log.txt", str(link) + "\n")
                pass
