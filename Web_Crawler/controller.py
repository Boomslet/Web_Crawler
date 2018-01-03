"""
User interface for the Crawler class

Author: Mark Boon
Date: 28/08/2017
Version: 2.0.0
"""

from crawler import *


def crawl(*urls):
    // load crawler threads
    for link in urls:
        current_worker = Worker(link)
        load = threading.Thread(target=current_worker.work)
        load.start()
