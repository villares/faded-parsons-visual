def has_free_lobe(f_allele, m_allele):
    """ Returns True only if both the father allele and the mother allele are "G".

    >>> has_free_lobe("G", "g")
    False
    >>> has_free_lobe("g", "G")
    False
    >>> has_free_lobe("g", "g")
    False
    >>> has_free_lobe("G", "G")
    True
    """