#!/usr/bin/env python3
"""
Python function that returns all students
sorted by average score
"""


def top_students(mongo_collection):
    """
    Function to return all students sorted by average

    Parameters: mongo_collection(collection object)

    Returns: average score(float)
    """
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "scores": 1,
                "averageScore": {"$avg": "$scores"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))
    for student in result:
        student["averageScore"] = round(student["averageScore"], 2)

    return result
