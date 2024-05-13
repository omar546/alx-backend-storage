#!/usr/bin/env python3
"""A Python function to update the topics of a school document based on its name.

Prototype: def update_topics(mongo_collection, name, topics):
The parameter 'mongo_collection' should be a pymongo collection object.
'name' (string) is the school name to be updated.
'topics' (list of strings) is the list of topics covered by the school.
"""
import pymongo

def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
