#!/usr/bin/env python3
"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    function that lists all documents in a collection

    Parameters: mongo_collection(object)

    Returns:
    empty list if no document in collection else
    returns a list of collections
    """
    collection = list(mongo_collection.find({}))
    return [col for col in collection]
