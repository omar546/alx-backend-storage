#!/usr/bin/env python3
"""A Python function to retrieve all documents from a MongoDB collection.

Prototype: def list_all(mongo_collection):
Returns an empty list if the collection is empty.
The parameter 'mongo_collection' should be a pymongo collection object.
"""
import pymongo

def list_all(mongo_collection):
    """Return list of all docs in collection"""
    if not mongo_collection:
        return []
    docs = mongo_collection.find()
    return [doc for doc in docs]
