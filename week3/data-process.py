import urllib.request as request
import json
import ssl
import re
import bs4
import sys
sys.path.append("modules")


import pttMovieCrawler as crawler
crawler.crawl(3)
import getOpenAPI as getData