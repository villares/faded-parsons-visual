def k_in_num(k, num):
    """
    >>> k_in_num(3, 123)  # Case 1
    True
    >>> k_in_num(5, 123)  # Case 2
    False
    >>> k_in_num(0, 0)  # Case 3
    False
    """
    while num:
        if k == num % 10:
            return True
        num = num // 10
    return False