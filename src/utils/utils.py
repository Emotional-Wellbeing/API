from typing import Collection


def inner_contained_fully_outer(inner: Collection, outer: Collection) -> bool:
    """
    Checks if all elements of inner collection are present in outer collection
    :param inner: Elements to check in outer
    :param outer: Collection that should contain all inner elements
    :return: true if all elements are present, otherwise false
    """
    return all(element in outer for element in inner)
