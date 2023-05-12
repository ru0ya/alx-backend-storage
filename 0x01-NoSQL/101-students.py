#!/usr/bin/env python3
"""
Function that returns all students sorted
by average score
"""


def top_students(mongo_collection):
    """function that returns all students stored
    by average score

    Parameters: mongo_collection(pymongo collection object)

    Returns: sorted average score
    """
    pipeline = [
        {
            '$project': {
                '_id': 1,
                'name': 1,
                'averageScore': {'$avg': '$topics.score'},
                'topics': 1,
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    students = mongo_collection.aggregate(pipeline)
    sorted_students = list(students)
    
    return sorted_students
