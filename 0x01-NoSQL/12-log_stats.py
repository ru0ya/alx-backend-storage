#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx
logs stored in MongoDB
"""

import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]

# Get total number of logs
total_logs = collection.count_documents({})
print(f"first line: {total_logs} logs where {total_logs} is the number of documents in this collection")

# Get counts for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
methods_counts = {}
for method in http_methods:
    count = collection.count_documents({"method": method})
    methods_counts[method] = count

print("second line: Methods:")
for method, count in methods_counts.items():
    print(f"\t{count} logs with method={method}")

# Get count for method=GET and path=/status
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})
print("method=GET")
print("path=/status")
print(get_status_count)

