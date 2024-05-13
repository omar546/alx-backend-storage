#!/usr/bin/env python3
"""A Python function to retrieve a list of schools that cover a specific topic.

Prototype: def schools_by_topic(mongo_collection, topic):
The parameter 'mongo_collection' should be a pymongo collection object.
'topic' (string) is the topic to search for.
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return mongo_collection.find({"topics": topic})
