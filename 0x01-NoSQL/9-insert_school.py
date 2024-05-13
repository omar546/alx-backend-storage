#!/usr/bin/env python3
"""A Python function to insert a new document into a collection based on keyword arguments.

Prototype: def insert_school(mongo_collection, **kwargs):
The parameter 'mongo_collection' should be a pymongo collection object.
Returns the new _id.
"""

import pymongo

def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection"""
    return mongo_collection.insert(kwargs)
