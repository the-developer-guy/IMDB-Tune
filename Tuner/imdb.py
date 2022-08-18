from scraper import get_movies
from adjuster import oscar_calculator, rating_penalizer

movies = get_movies()
top_movies = []

max_review_count = 0
for i in range(20):
    top_movies.append(movies[i])
    actual_review_count = movies[i]["rating"][1]
    if actual_review_count > max_review_count:
        max_review_count = actual_review_count

for movie in top_movies:
    oscar_calculator(movie)
    rating_penalizer(movie, max_review_count)
    print(f"Movie name: {movie['title']} rating: {movie['rating'][0]:.2f} adjusted: {movie['adjusted rating']:.2f} rating count: {movie['rating'][1]}")
