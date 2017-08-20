"""
User interface for the Crawler class

Author: Mark Boon
Date: 20/08/2017
Version: 1.3.1
"""

import threading
from Crawler import *

threadCount = int(input("Select number of threads to create: "))

threads = [None]*threadCount


for i in range(threadCount):
    threads[i] = Crawler(input("Enter base URL " + str(i+1) + ": "))
    
for i in range(threadCount):
    load = threading.Thread(target=threads[i].work)
    load.start()

