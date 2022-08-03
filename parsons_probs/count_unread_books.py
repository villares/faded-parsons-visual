def count_unread_books(books):
    """ Accepts a list of dicts describing books
    and returns the number of unread books in the list.

    >>> books = [{
    ...     "title": "Uncanny Valley",
    ...     "author": "Anna Wiener",
    ...     "read": False
    ...   }, {
    ...     "title": "Parable of the Sower",
    ...     "author": "Octavia E. Butler",
    ...     "read": True
    ...   }]
    >>> count_unread_books(books)
    1
    """