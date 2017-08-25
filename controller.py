"""
User interface for the Crawler class

Author: Mark Boon
Date: 23/08/2017
Version: 1.4.0
"""

import threading
from crawler import *


def crawl(threadCount):
    threads = [None]*threadCount

    for i in range(threadCount):
        currentWorker = threads[i]
        currentWorker = worker(input("Enter base URL " + str(i+1) + ": "))
        load = threading.Thread(target=currentWorker.work)
    load.start()
