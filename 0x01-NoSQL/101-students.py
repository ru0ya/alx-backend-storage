#!/usr/bin/env python3
"""
function that returns all students
sorted by average score
"""


def top_students(mongo_collection):
    """
    function that returns all students
    sorted by average score

    Parameters: mongo_collection(object)

    Returns: ordered list
    """
    students = list(mongo_collection.find())
    for student in students:
        scores = student["topics"]
        avgScore = {$avg: score}
        student["averageScore"] = avgScore

