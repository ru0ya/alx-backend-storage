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
    # updates topic based on name
    db = mongo_collection.update_many({"name": name},
                                     {"$set": {"topics": topics}})
    return db
