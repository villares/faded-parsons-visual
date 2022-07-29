def can_be_president(age, residency):
    """
    Returns whether someone can be US president based on age and residency.
    According to the US constitution, a presidential candidate must be at least
    35 years old and have been a US resident for at least 14 years.

    >>> can_be_president(30, 10)
    False
    >>> can_be_president(36, 10)
    False
    >>> can_be_president(30, 16)
    False
    >>> can_be_president(36, 15)
    True
    >>> can_be_president(36, 14)
    True
    >>> can_be_president(35, 14)
    True
    >>> can_be_president(35, 30)
    True
    """