def kth_divides_k(n, k):
    """
    >>> kth_divides_k(13, 1)  # Case 1
    True
    >>> kth_divides_k(12124, 2)  # Case 2
    True
    >>> kth_divides_k(1234, 3)  # Case 3
    True
    >>> kth_divides_k(53491, 4)  # Case 4
    False
    """
    index = 0
    while index < k:
        n = n // 10
        index = index + 1
    return (k % (n % 10)) == 0