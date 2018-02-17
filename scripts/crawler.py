import os
import sys
import requests
from bs4 import BeautifulSoup



class WebCrawler:
    def __init__(self, hostname):
        self._hostname = hostname

    def get_source(self):
        # get the website HTML source-code
        pass

    def parse_html(self, element, selector=None):
        pass

