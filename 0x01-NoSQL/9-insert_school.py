#!/usr/bin/env python3
"""
Insert a document in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts a new document in
    a collection based on kwargs

    Parameters: mongo_collection(object),
    **kwargs(string)

    Returns: new _id
    """
    doc = kwargs
    new_id = mongo_collection.insert_one(doc)

    return new_id

