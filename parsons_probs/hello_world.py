def hello_world(language_code):
    """ Returns the translation of "Hello, World" into the language
    specified by the language code (e.g. "es", "pt", "en"),
    defaulting to English if an unknown language code is specified.
    >>> hello_world("en")
    'Hello, World'
    >>> hello_world("es")
    'Hola, Mundo'
    >>> hello_world("pt")
    'Olá, Mundo'
    """