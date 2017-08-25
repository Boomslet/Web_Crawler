"""
User interface for the Crawler class

Author: Mark Boon
Date: 25/08/2017
Version: 1.5.0
"""

from crawler import *


def crawl(thread_count):
    for i in range(thread_count):
        current_worker = Worker(input("Enter base URL " + str(i + 1) + ": "))
        load = threading.Thread(target=current_worker.work)
        load.start()
