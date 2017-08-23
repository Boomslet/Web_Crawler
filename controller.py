"""
User interface for the Crawler class

Author: Mark Boon
Date: 23/08/2017
Version: 1.3.2
"""

import threading
from Crawler import *

threadCount = int(input("Select number of threads to create: "))
threads = [None]*threadCount

for i in range(threadCount):
    threads[i] = Crawler(input("Enter base URL " + str(i+1) + ": "))
    load = threading.Thread(target=threads[i].work)
    load.start()
