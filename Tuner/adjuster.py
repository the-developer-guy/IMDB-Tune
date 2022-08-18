def rating_penalizer(movie, top_rating_count):
    review_count_difference = top_rating_count - movie["rating"][1]
    if review_count_difference > 0:
        penalty = review_count_difference // 100000
        movie["adjusted rating"] -= penalty * 0.1


def oscar_calculator(movie):
    oscar_count = movie["oscar count"]
    rating_adjustment = 0
    if oscar_count == 1 or oscar_count == 2:
        rating_adjustment = 0.3
    elif oscar_count >= 3 and oscar_count <= 5:
        rating_adjustment = 0.5
    elif oscar_count >= 6 and oscar_count <= 10:
        rating_adjustment = 1.0
    elif oscar_count > 10:
        rating_adjustment = 1.5
    movie["adjusted rating"] += rating_adjustment
