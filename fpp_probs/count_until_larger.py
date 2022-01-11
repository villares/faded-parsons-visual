def count_until_larger(num):
    """
    >>> count_until_larger(117)  # .Case 1
    3
    >>> count_until_larger(8117)  # .Case 2
    3
    >>> count_until_larger(1118117)  # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(21)  # .Case 5
    1
    >>> count_until_larger(0)  # .Case 6
    0
    """
    rightmost = num % 10
    count = 0
    while num:
        if num % 10 > rightmost:
            return count
        num = num // 10
        count = count + 1
    return count 