from scraper import get_movies
from adjuster import oscar_calculator, rating_penalizer

movies = get_movies()

max_review_count = 0
for i in range(20):
    actual_review_count = movies[i]["rating count"]
    if actual_review_count > max_review_count:
        max_review_count = actual_review_count

for movie in movies:
    oscar_calculator(movie)
    rating_penalizer(movie, max_review_count)
    print(f"Movie name: {movie['title']} rating: {movie['rating']:.1f} adjusted: {movie['adjusted rating']:.1f} rating count: {movie['rating count']}")
