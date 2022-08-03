def count_multiples(start, end, divisor):
    """
    Counts the number of multiples of divisor between the start and end numbers.
    It should include the start or end if they are a multiple.

    >>> count_multiples(2, 2, 1)       # 2 is a multiple of 1
    1
    >>> count_multiples(2, 2, 2)       # 2 is a multiple of 2
    1
    >>> count_multiples(2, 2, 3)       # 2 is not a multiple of 3
    0
    >>> count_multiples(1, 12, 3)      # 3, 6, 9, 12
    4
    >>> count_multiples(237, 500, 10)
    27
    """
