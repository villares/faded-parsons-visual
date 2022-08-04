class MoviePurchase:
    """A class that represents movie purchases on YouTube,
    tracking the title and cost of each movie bought,
    as well as the number of times the movie is watched.

    >>> ponyo = MoviePurchase("Ponyo", 19.99)
    >>> ponyo.title
    'Ponyo'
    >>> ponyo.cost
    19.99
    >>> ponyo.times_watched
    0
    >>> ponyo.watch()
    >>> ponyo.watch()
    >>> ponyo.times_watched
    2
    """