from util import Card

def genres(movies):
    return {genres for movie in movies for genres in movie.genres}

def actors(movies):
    return {actors for movie in movies for actors in movie.actors}

def repeat_consecutive(xs, n):
    return [x for x in xs for y in range(n)]

def repeat_alternating(xs, n):
    return [x for y in range(n) for x in xs]

def cards(values, suits):
    return {Card(value, suit) for suit in suits for value in values}