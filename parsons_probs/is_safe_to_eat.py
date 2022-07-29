def is_safe_to_eat(seafood_type, days_frozen):
    """ Returns true if the seafood is safe to eat:
    either the type is "mollusk" or it's been frozen for at least 7 days.

    >>> is_safe_to_eat("tuna", 3)
    False
    >>> is_safe_to_eat("salmon", 6)
    False
    >>> is_safe_to_eat("salmon", 7)
    True
    >>> is_safe_to_eat("mollusk", 1)
    True
    >>> is_safe_to_eat("mollusk", 9)
    True
    """