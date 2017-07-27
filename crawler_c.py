import lxml
import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import util


class Crawler:
    base_url = ""
    domain = ""
    queue = []
    
    def __init__(self, base_url):
        Crawler.base_url = base_url
        Crawler.queue = [base_url]

    #
    def work(Crawler):
        
        for link in Crawler.queue:   
            try:
                util.create_dirs(link)
                page = urllib.request.urlopen(link)
                soup = BeautifulSoup(page, 'lxml')
                util.write_file("dump.txt", soup.text)
                
                for link in soup.find_all('a'):
                    dom = link['href']
                    dom = urljoin(Crawler.base_url, dom)
                    Crawler.queue.append(dom)
                        
            except:        
                pass

            

c = Crawler("https://www.pccasegear.com")
c.work()