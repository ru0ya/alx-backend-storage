#!/usr/bin/python3
"""
function that returns list of
school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    function that returns list of school
    having a specific topic

    Parameters: mongo_collection(object),
    topic(string)

    Returns: list
    """
    result = list(mongo_collection.find({"topic": topic}))
    return result
