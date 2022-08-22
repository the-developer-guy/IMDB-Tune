def rating_penalizer(rating_count, top_rating_count):
    review_count_difference = top_rating_count - rating_count
    rating_penalty = 0
    if review_count_difference > 0:
        penalty = review_count_difference // 100000
        rating_penalty = penalty * 0.1
    return rating_penalty


def oscar_calculator(oscar_count):
    rating_adjustment = 0
    if oscar_count == 1 or oscar_count == 2:
        rating_adjustment = 0.3
    elif oscar_count >= 3 and oscar_count <= 5:
        rating_adjustment = 0.5
    elif oscar_count >= 6 and oscar_count <= 10:
        rating_adjustment = 1.0
    elif oscar_count > 10:
        rating_adjustment = 1.5
    return rating_adjustment
