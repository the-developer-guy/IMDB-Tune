"""
IMDB scraper
"""

import urllib.request, urllib.error, urllib.parse


url = "https://www.imdb.com/chart/top/"
response = urllib.request.urlopen(url)
imdb_page = response.read().decode('UTF-8')
