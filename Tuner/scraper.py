"""
IMDB scraper
"""

import re
import urllib.request
from bs4 import BeautifulSoup


def get_page(url):
    response = urllib.request.urlopen(url)
    page = response.read().decode('UTF-8')
    tags = BeautifulSoup(page, 'html.parser')
    return tags


def get_rating_from_tag(tag):
    rating_tag = tag.find(class_="imdbRating")
    rating = rating_tag.contents[1]
    rating_string = rating.attrs["title"]
    parts = rating_string.split(" ")
    rating_value = float(parts[0])
    rating_count = int(parts[3].replace(",", ""))
    return rating_value, rating_count


def get_oscar_count(url):
    movie = get_page(url)
    tags = movie.find_all("a")
    for tag in tags:
        oscar_string = re.search("Won \d+ Oscar", str(tag.contents[0]))
        if oscar_string is not None:
            oscar_string_parts = oscar_string.group().split(" ")
            return int(oscar_string_parts[1])
    return 0


def get_movies(url="https://www.imdb.com/chart/top/", limit=20):
    movies = get_page(url)
    movies_table = movies.find(class_="lister-list")
    movies_list = []
    for movie_entry in movies_table.find_all("tr"):
        movie_model = {}
        movie_model["title"] = movie_entry\
            .find(class_="titleColumn")\
            .find("a").contents[0]
        movie_model["link"] = movie_entry.find("a")["href"]
        rating = get_rating_from_tag(movie_entry)
        movie_model["rating"] = rating[0]
        movie_model["rating count"] = rating[1]
        movie_model["adjusted rating"] = movie_model["rating"]
        movie_model["oscar count"] = get_oscar_count(f"https://www.imdb.com/{movie_model['link']}")
        movies_list.append(movie_model)
        if len(movies_list) >= limit:
            break
    return movies_list
