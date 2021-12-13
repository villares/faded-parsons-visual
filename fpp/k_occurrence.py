def k_occurence(k, num):
    """
    >>> k_occurence(5, 10)  # Case 1
    0
    >>> k_occurence(5, 5115)  # Case 2
    2
    >>> k_occurence(0, 100)  # Case 3
    2
    >>> k_occurence(0, 0)  # Case 4
    0
    """
    occurrences = 0
    while num:
        if num % 10 == k:
            occurrences += 1
        num = num // 10
    return occurrences   