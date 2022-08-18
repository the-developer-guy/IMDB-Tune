"""
IMDB scraper
"""

import urllib.request
from bs4 import BeautifulSoup


def get_rating_from_tag(tag):
    rating_tag = tag.find(class_="imdbRating")
    rating = rating_tag.contents[1]
    rating_string = rating.attrs["title"]
    parts = rating_string.split(" ")
    rating_value = float(parts[0])
    rating_count = int(parts[3].replace(",", ""))
    return rating_value, rating_count


def get_movies(url="https://www.imdb.com/chart/top/"):
    response = urllib.request.urlopen(url)
    imdb_page = response.read().decode('UTF-8')
    movies = BeautifulSoup(imdb_page, 'html.parser')

    movies_table = movies.find(class_="lister-list")
    movies_list = []
    for movie_entry in movies_table.find_all("tr"):
        movie_model = {}
        movie_model["title"] = movie_entry\
            .find(class_="titleColumn")\
            .find("a").contents[0]
        movie_model["link"] = movie_entry.find("a")["href"]
        movie_model["rating"] = get_rating_from_tag(movie_entry)
        movie_model["adjusted rating"] = movie_model["rating"][0]
        movie_model["oscar count"] = 0
        movies_list.append(movie_model)
    return movies_list
