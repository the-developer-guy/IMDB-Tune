"""
IMDB scraper
"""

import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup


url = "https://www.imdb.com/chart/top/"
response = urllib.request.urlopen(url)
imdb_page = response.read().decode('UTF-8')
movies = BeautifulSoup(imdb_page, 'html.parser')

movies_table = movies.find(class_="lister-list")
movie_links = []
for tag in movies_table.find_all("tr"):
    movie_links.append(tag.find("a")["href"])
