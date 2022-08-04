class Plant:
    """A class used by a plant nursery to track what plants they have in inventory
    and how many they have of each plant.

    >>> milkweed = Plant("Narrow-leaf milkweed", "Asclepias fascicularis")
    >>> milkweed.common_name
    'Narrow-leaf milkweed'
    >>> milkweed.latin_name
    'Asclepias fascicularis'
    >>> milkweed.inventory
    0
    >>> milkweed.update_inventory(2)
    >>> milkweed.inventory
    2
    >>> milkweed.update_inventory(3)
    >>> milkweed.inventory
    5
    """
