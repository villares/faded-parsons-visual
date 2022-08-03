def contains_15row(grid):
    """Takes an input of a 2-dimensional list of numbers
        and returns true if any of the rows add up to 15.

    >>> grid1 = [
    ...     [5, 1, 6],   # 12
    ...     [10, 4, 1],  # 15!!
    ...     [8, 3, 2]    # 13
    ... ]
    >>> contains_15row(grid1)
    True
    >>> grid2 = [
    ...     [15, 1, 6], # 22
    ...     [10, 4, 0], # 14
    ...     [8, 3, 2]   # 13
    ... ]
    >>> contains_15row(grid2)
    False
    """