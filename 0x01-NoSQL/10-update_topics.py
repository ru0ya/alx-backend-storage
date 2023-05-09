#!/usr/bin/env python3
"""
Makes changes
"""


def update_topics(mongo_collection, name, topics):
    """
    Function that changes all topics
    of a school based on name

    Parameters: mongo_collection(object),
    name(string),
    topics(list of strings)

    Returns: updated list
    """
    db = mongo_collection.update_one({"name": name}, {"$set":{"topics": topics}})  # updates topic depending on the name
    return db

