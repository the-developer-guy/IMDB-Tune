import csv
from scraper import get_movies
from adjuster import oscar_calculator, rating_penalizer

movies = get_movies()

max_review_count = 0
for i in range(20):
    actual_review_count = movies[i]["rating count"]
    if actual_review_count > max_review_count:
        max_review_count = actual_review_count

with open("top 20 IMDB movies.csv", "wt", encoding="utf-8", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["title", "rating", "adjusted rating"])
    for movie in movies:
        movie["adjusted rating"] += oscar_calculator(movie["oscar count"])
        movie["adjusted rating"] -= rating_penalizer(movie["rating count"], max_review_count)
        row = [movie["title"]]
        row.append(f"{movie['rating']:.1f}")
        row.append(f"{movie['adjusted rating']:.1f}")
        writer.writerow(row)
