__author__ = 'rubanenko'

from .user import User
from math import sqrt
from time import clock

memoryzation_map = {}


def get_elo_win_probability(ra, rb):
    return 1.0 / (1.0 + 10.0 ** ((rb - ra) / 400.0))


def get_seed(contestants, rating):
    if rating in memoryzation_map:
        return memoryzation_map[rating]
    result = 1.0
    for contestant in contestants:
        result += get_elo_win_probability(contestant.rating, rating)
    memoryzation_map[rating] = result
    return result


def get_rating_to_rank(contestants, rank):
    left  = 1
    right = 8000
    while right - left > 1:
        mid = (left + right) // 2
        if get_seed(contestants, mid) < rank:
            right = mid
        else:
            left = mid
    return left


def reassign_ranks(contestants):
    contestants.sort(key=lambda contestant: contestant.place)
    first = 0
    place = contestants[0].place
    for i in range(1, len(contestants)):
        if contestants[i].place > place:
            for j in range(first, i):
                contestants[j].place = i
            first = i
            place = contestants[i].place
    for i in range(first, len(contestants)):
        contestants[i].place = len(contestants)

def process(contestants):
    if len(contestants) == 0:
        return
    reassign_ranks(contestants)
    for i in range(len(contestants)):
        contestants[i].seed = 1.0
        for j in range(len(contestants)):
            if i != j:
                contestants[i].seed += get_elo_win_probability(contestants[j].rating, contestants[i].rating)
    for i in range(len(contestants)):
        mid_rank              = sqrt(contestants[i].place * contestants[i].seed)
        need_rating           = get_rating_to_rank(contestants, mid_rank)
        contestants[i].delta  = (need_rating - contestants[i].rating) // 2

    contestants.sort(key=lambda contestant: contestant.rating, reverse=True)

    sum_of_deltas = 0
    for contestant in contestants:
        sum_of_deltas += contestant.delta
    inc = -sum_of_deltas // len(contestants) - 1
    for i in range(len(contestants)):
        contestants[i].delta += inc
    sum_of_deltas  = 0
    zero_sum_count = min(int(4 * round(sqrt(len(contestants)))), len(contestants))
    for i in range(zero_sum_count):
        sum_of_deltas += contestants[i].delta

    inc = min(max(-sum_of_deltas // zero_sum_count, -10),  0)
    for i in range(len(contestants)):
        contestants[i].delta += inc


def calculate_rating_change(users):
    start_time = clock()
    process(users)
    result = {}
    for user in users:
        result[user.id] = user.delta + user.rating
    return result
