def calculate_lifetime_supply(age, num_per_day):
    """ Returns the amount of items consumed over a lifetime
    (with a max age of 100 assumed) based on the current age
    and the number consumed per day.

    >>> calculate_lifetime_supply(99, 1)
    365
    >>> calculate_lifetime_supply(99, 2)
    730
    >>> calculate_lifetime_supply(36, 3)
    70080
    """